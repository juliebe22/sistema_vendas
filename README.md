# 🛒 Sistema de Vendas

> Sistema desenvolvido para gerenciamento de vendas, controle de estoque e consulta de relatórios.

---

## 📌 Sobre o projeto

O **Sistema de Vendas** é uma aplicação desenvolvida em Python integrada a um banco de dados PostgreSQL.

O sistema permite registrar vendas, controlar automaticamente o estoque dos produtos e consultar um relatório com as vendas realizadas.

O projeto também utiliza recursos do PostgreSQL, como **Function, Procedure e View**, integrados à aplicação.

---

## 🎯 Objetivo

Desenvolver uma aplicação integrada a banco de dados capaz de realizar operações relacionadas ao registro de vendas, utilizando recursos de programação e recursos avançados do PostgreSQL.

---

## ⚙️ Funcionalidades

### 🛍️ Registro de vendas

Permite selecionar um produto, informar a quantidade e escolher a forma de pagamento.

### 📦 Controle de estoque

Após uma venda, o estoque do produto é atualizado automaticamente.

### 📊 Relatório de vendas

Apresenta as vendas realizadas utilizando uma View do banco de dados.

### 🧮 Cálculo do valor total

O valor total da venda é calculado através de uma Function criada no PostgreSQL.

### 💰 Registro de movimentações

As vendas realizadas também são registradas na tabela de movimentações financeiras.

---

## 🗄️ Recursos do Banco de Dados

### 🔹 Function — `calcular_total`

Recebe o preço do produto e a quantidade vendida e retorna o valor total da venda.

**Parâmetros:**

- `p_preco` — preço do produto;
- `p_quantidade` — quantidade vendida.

**Retorno:** valor total da venda.

---

### ⚙️ Procedure — `registrar_venda`

A procedure `registrar_venda` é responsável por realizar o processo completo de registro de uma venda.

**Parâmetros:**

- `p_id_produto` — identificação do produto;
- `p_quantidade` — quantidade vendida;
- `p_forma_pagamento` — forma de pagamento utilizada.

Durante a execução, a procedure:

- verifica se o produto existe;
- verifica se há estoque suficiente;
- valida a quantidade informada;
- utiliza a Function `calcular_total` para calcular o valor da venda;
- registra a venda na tabela `vendas`;
- atualiza o estoque do produto;
- registra a movimentação financeira.

---

### 👁️ View — `vw_relatorio_vendas`

A View `vw_relatorio_vendas` foi criada para facilitar a consulta das vendas realizadas.

Ela relaciona as tabelas `vendas` e `produtos` e disponibiliza as seguintes informações:

- ID da venda;
- data da venda;
- nome do produto;
- quantidade;
- preço unitário;
- valor total;
- forma de pagamento.

A aplicação utiliza essa View para apresentar o **Relatório de Vendas** ao usuário.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 **Python** | Desenvolvimento da aplicação |
| 🖥️ **Tkinter** | Criação da interface gráfica |
| 🐘 **PostgreSQL** | Banco de dados |
| 🔗 **Psycopg2** | Conexão entre Python e PostgreSQL |
| 📋 **SQL** | Criação e manipulação das estruturas do banco |
| ⚙️ **PL/pgSQL** | Desenvolvimento da Function e Procedure |
| 🌐 **GitHub** | Versionamento e armazenamento do projeto |

---

## 📁 Estrutura do projeto

A organização dos arquivos do projeto está dividida entre a aplicação Python e os scripts do banco de dados.

**sistema-vendas/**
- 📂 **src/**
  - `database.py`
  - `main.py`
  - `produtos.py`
  - `relatorio.py`
  - `vendas.py`
- 📂 **database/**
  - 📂 **tables/**
    - `tabelas.sql`
  - 📂 **inserts/**
    - `dados.sql`
  - 📂 **functions/**
    - `calcular_total.sql`
  - 📂 **procedures/**
    - `registrar_venda.sql`
  - 📂 **views/**
    - `vw_relatorio_vendas.sql`
- `README.md`

---

## 🚀 Como executar

### 1. Requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3
- PostgreSQL
- Git

### 2. Clonar o projeto

No terminal, execute:

    git clone URL_DO_REPOSITORIO

Depois, entre na pasta do projeto:

    cd sistema-vendas

### 3. Criar o banco de dados

No PostgreSQL, crie um banco de dados chamado:

    sistema_vendas

### 4. Executar os scripts SQL

Execute os scripts na seguinte ordem:

1. `database/tables/tabelas.sql`
2. `database/inserts/dados.sql`
3. `database/functions/calcular_total.sql`
4. `database/procedures/registrar_venda.sql`
5. `database/views/vw_relatorio_vendas.sql`

### 5. Instalar a dependência

Abra o terminal na pasta do projeto e execute:

    pip install psycopg2-binary

### 6. Configurar a conexão com o banco

No arquivo `src/database.py`, configure os dados de acesso ao PostgreSQL:

    import psycopg2

    def conectar():
        return psycopg2.connect(
            host="localhost",
            database="sistema_vendas",
            user="postgres",
            password="SUA_SENHA",
            port="5432"
        )

Substitua `SUA_SENHA` pela senha configurada no PostgreSQL.

### 7. Executar o sistema

Entre na pasta `src`:

    cd src

Depois execute:

    python main.py

O sistema será aberto em uma janela gráfica.

---

## 🔄 Funcionamento do sistema

O fluxo principal do sistema ocorre da seguinte forma:

    👤 Usuário
        ↓
    🖥️ Interface gráfica em Python
        ↓
    🗄️ Banco de dados PostgreSQL
        ↓
    ⚙️ Procedure registrar_venda
        ↓
    🧮 Function calcular_total
        ↓
    📦 Atualização do estoque
        ↓
    💰 Registro da venda
        ↓
    📊 View vw_relatorio_vendas
        ↓
    🖥️ Exibição do relatório

Ao registrar uma venda, a aplicação envia os dados para a Procedure `registrar_venda`.

A Procedure realiza as validações necessárias, utiliza a Function para calcular o valor total, registra a venda, atualiza o estoque e registra a movimentação financeira.

Posteriormente, o usuário pode consultar as vendas realizadas através do relatório, que utiliza a View `vw_relatorio_vendas`.

---

## 📚 Objetivo acadêmico

Este projeto foi desenvolvido como atividade acadêmica com o objetivo de aplicar conhecimentos de **Banco de Dados, SQL, PL/pgSQL, programação em Python e integração entre aplicação e banco de dados**.

O projeto demonstra a utilização prática de **Function, Procedure e View** em uma aplicação integrada a um banco de dados PostgreSQL.

---
## 📷 Vídeo explicativo 

https://drive.google.com/drive/folders/19ijt6m0VH36XajvYhE5XkPWuegUReADD?usp=sharing
