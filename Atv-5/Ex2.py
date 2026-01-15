def verificar_palindromo(texto):
    texto_limpo = ""
    for char in texto:
        if char.isalnum():
            texto_limpo += char.lower()
    
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

texto = input("Digite um texto: ")
resultado = verificar_palindromo(texto)
print(resultado)