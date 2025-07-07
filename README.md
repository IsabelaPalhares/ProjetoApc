# CRUD de Animais em Extinção no Brasil

![Badge](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Badge](https://img.shields.io/badge/python-3.9%2B-blue)
![Badge](https://img.shields.io/badge/framework-Flask-black)

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
* **Seção de Conscientização:** Uma área dedicada a informar os usuários sobre como podem ajudar a prevenir a extinção de espécies.
* **Persistência de Dados com SQLAlchemy:** Utiliza o ORM SQLAlchemy para mapear objetos Python para o banco de dados SQLite, simplificando as operações e garantindo a integridade dos dados.
* **Script de Semeadura (Seed):** Inclui um script para popular o banco de dados inicial a partir de um arquivo CSV, facilitando a configuração inicial do ambiente.

---

## 3. Tecnologias Utilizadas

* **Backend:** Python 3
* **Framework:** Flask
* **Banco de Dados/ORM:** SQLAlchemy com SQLite
* **Frontend:** HTML5, CSS3

---

## 4. Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### **Pré-requisitos**

Antes de começar, garanta que você tenha o **Python 3** instalado em sua máquina.

### **Instalação**
1.  **Instale as dependências:**
    O projeto utiliza as bibliotecas Flask e Flask-SQLAlchemy. Instale-as com o seguinte comando:
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

### **Configuração do Banco de Dados**

Para que a aplicação funcione corretamente, é necessário popular o banco de dados. O script `seed.py` foi criado para isso, lendo os dados do arquivo `Fauna Ameaçada.csv`.

1.  Execute o script de semeadura:
    ```bash
    python3 seed.py
    ```
    Aguarde a mensagem de confirmação no terminal, que indicará que os animais foram adicionados com sucesso.

### **Iniciando a Aplicação**

Com o ambiente e o banco de dados configurados, você já pode iniciar o servidor.

1.  Execute o arquivo principal da aplicação:
    ```bash
    python3 app.py
    ```

2.  Abra seu navegador e acesse a seguinte URL:
    ```
    [http://127.0.0.1:5153/]
    ```

Pronto! A aplicação estará rodando em sua máquina local.

---


