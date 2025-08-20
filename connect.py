import psycopg2
import os
import time
import mysql.connector

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'carga')
DB_USER = os.getenv('DB_USER', 'vinicius')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'vinicius')
DB_PORT = os.getenv('DB_PORT', '5432')

DB_HOST_SQL = os.getenv('DB_HOST', 'localhost')
DB_NAME_SQL = os.getenv('MYSQL_DATABASE', 'migracao')
DB_USER_SQL = os.getenv('MYSQL_USER', 'vinicius')
DB_PASSWORD_SQL = os.getenv('MYSQL_PASSWORD', 'vinicius')
DB_PORT_SQL = os.getenv('DB_PORT', 3306)


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

def connect_to_mysql():
    conn = None
    tentativas = 5
    while tentativas > 0:
        try:
            print(f'Tentando conectar ao banco de dados em {DB_HOST_SQL}:{DB_NAME_SQL} como {DB_USER_SQL}...')
            conn = mysql.connector.connect(
                host=DB_HOST_SQL,
                port=DB_PORT_SQL,
                database=DB_NAME_SQL,
                user=DB_USER_SQL,
                password=DB_PASSWORD_SQL
            )
            print('Conexão com o Mysql estabelecida com sucesso')
            return conn
        except mysql.connector.Error as e:
            print(F'Erro ao conectar{e}')
            tentativas -= 1
            if tentativas > 0:
                print(f"Tentando novamente em 5 segundos... ({tentativas} tentativas restantes)")
                time.sleep(5)
            else:
                print("Número máximo de tentativas de conexão atingido.")
                raise e
        except Exception as e:
            print(f"Um erro inesperado ocorreu: {e}")
            raise e
        return None