from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do SQLAlchemy para interagir com o banco.
db = SQLAlchemy()

# Define a estrutura (modelo) da tabela de animais no banco de dados.
class Task(db.Model):
    # Define as colunas da tabela e seus tipos de dados.
    id = db.Column(db.Integer, primary_key=True) # ID único para cada animal.
    nome = db.Column(db.String(100), unique=False, nullable=False) # Nome popular do animal.
    nome_cientifico = db.Column(db.String(100), unique=True, nullable=False) # Nome científico (deve ser único).
    status = db.Column(db.String(100), unique=False, nullable=False) # Status de conservação.
    regiao = db.Column(db.String(100), unique=False, nullable=False) # Regiões onde é encontrado.
    bioma = db.Column(db.String(100), unique=False, nullable=False) # Biomas que habita.

    def __repr__(self):
        return f'<Task {self.id}>'