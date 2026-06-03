import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        return "Tamanho mínimo é 4"

    # garante requisitos básicos
    maiuscula = random.choice(string.ascii_uppercase)
    minuscula = random.choice(string.ascii_lowercase)
    numero = random.choice(string.digits)
    simbolo = random.choice("!@#$%&*")

    resto = string.ascii_letters + string.digits + "!@#$%&*"

    senha = [
        maiuscula,
        minuscula,
        numero,
        simbolo
    ]

    for _ in range(tamanho - 4):
        senha.append(random.choice(resto))

    random.shuffle(senha)

    return "".join(senha)


while True:
    print("\n=== GERADOR DE SENHAS SEGURAS ===")

    try:
        tamanho = int(input("Digite o tamanho da senha (0 para sair): "))

        if tamanho == 0:
            print("Saindo...")
            break

        senha = gerar_senha(tamanho)

        print(f"\nSenha gerada: {senha}")

    except ValueError:
        print("Digite apenas números!")
