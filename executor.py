import carga
import connect


def executa(operacao):

    pg_conn = None
    my_conn = None

    try:

        pg_conn = connect.connect_to_db()
        my_conn = connect.connect_to_mysql()

        if operacao == "select":
            carga.select_dados(pg_conn)
        elif operacao == "migraco":
            carga.migrar_dados(pg_conn, my_conn)
        else:
            carga.incluir_dados(pg_conn)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if pg_conn:
            pg_conn.close()
        elif my_conn:
              my_conn.close()

if __name__ == "__main__":
    executa("migraco")