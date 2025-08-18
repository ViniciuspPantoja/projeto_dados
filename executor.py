import carga
import connect


def executa(operacao):

    conn = None

    try:

        conn = connect.connect_to_db()

        if operacao == "select":
            carga.select_dados(conn)
        else:
            carga.incluir_dados(conn)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    executa("select")