import requests

def consultar_moeda():
    moeda = input("Digite a sigla da moeda para converter em Real (ex: USD, EUR, BTC): ").upper()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        chave = f"{moeda}BRL"
        info = dados[chave]
        
        print(f"Moeda: {info['name']}")
        print(f"Valor Atual: R$ {info['bid']}")
        print(f"Máxima: R$ {info['high']}")
        print(f"Mínima: R$ {info['low']}")
        print(f"Data/Hora: {info['create_date']}")
        
    except (requests.exceptions.RequestException, KeyError):
        print("Erro: Moeda não encontrada ou falha na conexão.")

consultar_moeda()