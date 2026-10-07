import tkinter as tk
from tkinter import ttk
from database import conectar


def listar_vendas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id_venda,
            data,
            produto,
            quantidade,
            preco_unitario,
            valor_total,
            forma_pagamento
        FROM vw_relatorio_vendas
    """)

    vendas = cursor.fetchall()

    cursor.close()
    conexao.close()

    return vendas


def abrir_tela_relatorio(janela_principal):

    tela = tk.Toplevel(janela_principal)
    tela.title("Relatório de Vendas")
    tela.geometry("950x450")

    titulo = tk.Label(
        tela,
        text="RELATÓRIO DE VENDAS",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=20)

    colunas = (
        "ID",
        "Data",
        "Produto",
        "Quantidade",
        "Preço",
        "Total",
        "Pagamento"
    )

    tabela = ttk.Treeview(
        tela,
        columns=colunas,
        show="headings"
    )

    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=120)

    tabela.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=10
    )

    vendas = listar_vendas()

    for venda in vendas:
        tabela.insert(
            "",
            tk.END,
            values=venda
        )