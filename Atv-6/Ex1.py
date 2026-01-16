import random
import string

def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Sua nova senha é: {senha}")

gerar_senha()