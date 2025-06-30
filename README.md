# CRUD de Animais em Extinção no Brasil

## 1. Descrição do Projeto

O projeto **CRUD de Animais em Extinção** é uma aplicação web desenvolvida em Python com o framework Flask. Ele permite o gerenciamento completo (Cadastro, Leitura, Atualização e Exclusão) de uma base de dados de animais ameaçados de extinção, com foco nos biomas brasileiros.

A aplicação foi desenvolvida como parte da disciplina de Algoritmos e Programação de Computadores (APC) na Universidade de Brasília (UnB), com o objetivo de criar uma ferramenta funcional, informativa e de conscientização sobre a fauna brasileira.

**Integrantes:**
* Isabela Palhares Lage
* Maria Júlia Batista
* Pedro Henrique Mesquita
* Vinicius Viana

---

## 2. Funcionalidades Principais

* **CRUD Completo:** Crie, visualize, edite e remova registros de animais da base de dados.
* **Filtro por Bioma:** Filtre a visualização dos animais por biomas específicos (Amazônia, Cerrado, Mata Atlântica, etc.) através de um menu suspenso populado dinamicamente.
* **Paginação:** A lista de animais é paginada para garantir uma navegação fluida, mesmo com uma grande quantidade de dados.
* **Persistência de Dados com SQLAlchemy:** Utiliza o ORM SQLAlchemy para mapear objetos Python para o banco de dados SQLite, simplificando as operações e garantindo a integridade dos dados.
* **Script de Semeadura (Seed):** Inclui um script para popular o banco de dados inicial a partir de um arquivo CSV, facilitando a configuração inicial do ambiente.

---

## 3. Tecnologias Utilizadas

* **Backend:** Python 3
* **Framework:** Flask
* **Banco de Dados/ORM:** SQLAlchemy com SQLite
* **Frontend:** HTML5, CSS3

---
