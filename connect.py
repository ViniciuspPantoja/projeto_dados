import psycopg2
import os
import time

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'carga')
DB_USER = os.getenv('DB_USER', 'vinicius')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'vinicius')
DB_PORT = os.getenv('DB_PORT', '5432')

def connect_to_db():
    conn = None
    retries = 5
    while retries > 0:
        try:
            print(f"Tentando conectar ao banco de dados em {DB_HOST}:{DB_NAME} como {DB_USER}...")
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                port=DB_PORT
            )
            print("Conexão com o PostgreSQL estabelecida com sucesso!")
            return conn
        except psycopg2.Error as e:
            print(f"Erro ao conectar: {e}")
            retries -= 1
            if retries > 0:
                print(f"Tentando novamente em 5 segundos... ({retries} tentativas restantes)")
                time.sleep(5)
            else:
                print("Número máximo de tentativas de conexão atingido.")
                raise e
        except Exception as e:
            print(f"Um erro inesperado ocorreu: {e}")
            raise e
    return None