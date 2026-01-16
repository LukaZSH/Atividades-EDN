import requests

def buscar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
        
    except requests.exceptions.RequestException:
        print("Falha na conexão ao buscar usuário.")

buscar_usuario_aleatorio()