from database import conectar


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_produto, nome, preco, estoque
        FROM produtos
        ORDER BY id_produto
    """)

    produtos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return produtos