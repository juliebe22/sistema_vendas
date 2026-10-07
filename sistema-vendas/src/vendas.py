import tkinter as tk
from tkinter import messagebox, ttk
from database import conectar


def buscar_produtos():
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


def registrar_venda(id_produto, quantidade, forma_pagamento):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            CALL registrar_venda(%s, %s, %s)
            """,
            (id_produto, quantidade, forma_pagamento)
        )

        conexao.commit()

        return True, "Venda registrada com sucesso!"

    except Exception as erro:
        conexao.rollback()
        return False, str(erro)

    finally:
        cursor.close()
        conexao.close()


def abrir_tela_vendas(janela_principal):

    tela = tk.Toplevel(janela_principal)
    tela.title("Registrar Venda")
    tela.geometry("450x450")
    tela.resizable(False, False)

    titulo = tk.Label(
        tela,
        text="REGISTRAR VENDA",
        font=("Arial", 20, "bold")
    )
    titulo.pack(pady=20)

    # Buscar produtos no banco
    produtos = buscar_produtos()

    # Dicionário para relacionar o nome exibido ao ID
    produtos_dict = {}

    for produto in produtos:
        id_produto = produto[0]
        nome = produto[1]
        preco = produto[2]
        estoque = produto[3]

        texto = f"{nome} - R$ {preco:.2f} (Estoque: {estoque})"

        produtos_dict[texto] = id_produto

    # Produto
    tk.Label(
        tela,
        text="Produto:"
    ).pack()

    combo_produtos = ttk.Combobox(
        tela,
        values=list(produtos_dict.keys()),
        state="readonly",
        width=40
    )

    combo_produtos.pack(pady=8)

    if produtos:
        combo_produtos.current(0)

    # Quantidade
    tk.Label(
        tela,
        text="Quantidade:"
    ).pack()

    entrada_quantidade = tk.Entry(tela)
    entrada_quantidade.pack(pady=8)

    # Forma de pagamento
    tk.Label(
        tela,
        text="Forma de pagamento:"
    ).pack()

    combo_pagamento = ttk.Combobox(
        tela,
        values=["PIX", "Dinheiro", "Cartão de Crédito", "Cartão de Débito"],
        state="readonly",
        width=30
    )

    combo_pagamento.pack(pady=8)
    combo_pagamento.current(0)

    def confirmar():

        try:
            produto_selecionado = combo_produtos.get()

            if not produto_selecionado:
                messagebox.showwarning(
                    "Atenção",
                    "Selecione um produto."
                )
                return

            id_produto = produtos_dict[produto_selecionado]

            quantidade = int(entrada_quantidade.get())

            if quantidade <= 0:
                messagebox.showwarning(
                    "Atenção",
                    "A quantidade deve ser maior que zero."
                )
                return

            forma_pagamento = combo_pagamento.get()

            sucesso, mensagem = registrar_venda(
                id_produto,
                quantidade,
                forma_pagamento
            )

            if sucesso:
                messagebox.showinfo(
                    "Sucesso",
                    mensagem
                )

                tela.destroy()

            else:
                messagebox.showerror(
                    "Erro",
                    mensagem
                )

        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe uma quantidade válida."
            )

    botao = tk.Button(
        tela,
        text="Registrar Venda",
        font=("Arial", 12),
        width=20,
        command=confirmar
    )

    botao.pack(pady=25)