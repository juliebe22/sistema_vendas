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

## 🗄️ Recursos do PostgreSQL

O projeto utiliza três recursos principais do banco de dados:

### 🔹 Function — `calcular_total`

Recebe o preço do produto e a quantidade vendida e retorna o valor total da venda.

```sql
calcular_total(preco, quantidade)
