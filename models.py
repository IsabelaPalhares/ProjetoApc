from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=False, nullable=False)
    nome_cientifico = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(100), unique=False, nullable=False)
    regiao = db.Column(db.String(100), unique=False, nullable=False)
    bioma = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.id}>'