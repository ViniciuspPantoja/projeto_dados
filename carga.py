import dadosArquivo

def incluir_dados (conn):

    try:
        cur = conn.cursor()

        sql_insert = """
                     INSERT INTO organizacao_dados (organizacao, nome, descricao, tags, quantidade_recursos)
                     VALUES (%s, %s, %s,%s, %s); 
                     """

        infos = dadosArquivo.ler_arquivo("conjunto-dados.csv")
        for index, linha in infos:
            organizacao = linha['Organização']
            nomes = linha['Nome']
            descricao = linha['Descrição']
            tags = linha['Tags']
            quantidadeRecursos = linha['Quantidade Recursos']

            cur.execute(sql_insert, (organizacao, nomes, descricao, tags, quantidadeRecursos))

        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        if cur:
            cur.close()

def select_dados(conn):

    try:
        cur = conn.cursor()

        sql_select = """
                     SELECT * FROM organizacao_dados;
                     """

        cur.execute(sql_select)
        rows = cur.fetchall()

        return rows

    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
    finally:
        if cur:
            cur.close()


def migrar_dados(pg_conn, my_conn):
    pg = None
    my = None

    try:
        pg = pg_conn.cursor()
        my = my_conn.cursor()

        rows = select_dados(pg_conn)

        print("PASSEI AQUI")

        print(rows)

        #print(f"{len(rows)} registros encontrados no PostgreSQL.")

        sql_insert = """
            INSERT INTO organizacao_dados (organizacao, nome, descricao, tags, quantidade_recursos,quantidade_reusos ,quantidade_downloads, quantidade_seguidores, data_criacao )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        for i, row in enumerate(rows, start=1):

            try:

                my.execute(sql_insert, row)
            except Exception as e:
                print(f"Erro ao inserir registro {i}: {e}")

        my_conn.commit()
        print("Migração concluída com sucesso!")

    except Exception as e:
        if my_conn:
            my_conn.rollback()
        print(f"Erro geral na migração: {e}")

    finally:
        if pg:
            pg.close()
        if my:
            my.close()
        print("Cursores fechados com segurança.")
