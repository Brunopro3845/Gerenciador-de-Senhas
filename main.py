import json
import random
import string
import os

ARQUIVO = "senhas.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return {}

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except:
        return {}


def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def gerar_senha(tamanho):
    if tamanho < 4:
        return None

    senha = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%&*")
    ]

    caracteres = (
        string.ascii_letters +
        string.digits +
        "!@#$%&*"
    )

    for _ in range(tamanho - 4):
        senha.append(random.choice(caracteres))

    random.shuffle(senha)

    return "".join(senha)


def adicionar_conta():
    dados = carregar_dados()

    site = input("Site/Serviço: ").strip()

    if site in dados:
        print("⚠️ Essa conta já existe.")
        return

    usuario = input("Usuário: ").strip()

    try:
        tamanho = int(input("Tamanho da senha: "))
    except ValueError:
        print("Digite apenas números.")
        return

    senha = gerar_senha(tamanho)

    if senha is None:
        print("A senha deve ter pelo menos 4 caracteres.")
        return

    dados[site] = {
        "usuario": usuario,
        "senha": senha
    }

    salvar_dados(dados)

    print("\n✅ Conta salva com sucesso!")
    print("Senha gerada:", senha)


def listar_contas():
    dados = carregar_dados()

    if not dados:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=== CONTAS SALVAS ===")

    for site, info in dados.items():
        print(f"\nSite: {site}")
        print(f"Usuário: {info['usuario']}")
        print(f"Senha: {info['senha']}")


def buscar_conta():
    dados = carregar_dados()

    site = input("Digite o nome do site: ").strip()

    if site not in dados:
        print("Conta não encontrada.")
        return

    print("\n=== CONTA ENCONTRADA ===")
    print("Site:", site)
    print("Usuário:", dados[site]["usuario"])
    print("Senha:", dados[site]["senha"])


def remover_conta():
    dados = carregar_dados()

    site = input("Conta a remover: ").strip()

    if site not in dados:
        print("Conta não encontrada.")
        return

    del dados[site]

    salvar_dados(dados)

    print("✅ Conta removida com sucesso.")


def menu():
    while True:
        print("\n" + "=" * 35)
        print("   GERENCIADOR DE SENHAS")
        print("=" * 35)
        print("1 - Adicionar conta")
        print("2 - Listar contas")
        print("3 - Buscar conta")
        print("4 - Remover conta")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_conta()

        elif opcao == "2":
            listar_contas()

        elif opcao == "3":
            buscar_conta()

        elif opcao == "4":
            remover_conta()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
