import pandas as pd

def ler_arquivo(arquivo):
    try:
        df = pd.read_csv(arquivo, sep=';', encoding='utf-8-sig')
        return df.iterrows()

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
