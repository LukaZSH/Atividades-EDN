import pandas as pd

try:
    df = pd.read_csv('logs_treinamento.csv')
    media = df['tempo_execucao'].mean()
    desvio_padrao = df['tempo_execucao'].std()
    
    print(f"Média: {media}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Erro na leitura do arquivo: {e}")