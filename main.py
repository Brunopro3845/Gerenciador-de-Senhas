import random
import string

def gerar_senha(tamanho=12):
    if tamanho < 4:
        return "Tamanho mínimo é 4 caracteres"

    caracteres = string.ascii_letters + string.digits + "!@#$%&*"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


print("=== GERADOR DE SENHAS SPARK 2030 ===")

try:
    tamanho = int(input("Quantos caracteres quer na senha? "))
    senha_gerada = gerar_senha(tamanho)

    print(f"\nSua senha segura: {senha_gerada}")
    print("\nNunca use a mesma senha em vários sites!")

except ValueError:
    print("Erro: digite apenas números!")
