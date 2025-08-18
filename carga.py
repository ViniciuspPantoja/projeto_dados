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

        for row in rows:
            print(row)

    except Exception as e:
        print(f"Erro ao consultar dados: {e}")
    finally:
        if cur:
            cur.close()