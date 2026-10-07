import psycopg2


def conectar():
    return psycopg2.connect(
        host="localhost",
        database="sistema_vendas",
        user="postgres",
        password="root",
        port="5432"
    )