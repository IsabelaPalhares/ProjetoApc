from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    nome_cientifico = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(100), unique=False, nullable=False)
    regiao = db.Column(db.String(100), unique=False, nullable=False)
    bioma = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/')
def index():
    tasks = Tasks.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/create", methods=["POST"])
def create_task():
    nome = request.form["nome"]
    new_task = Tasks(nome = nome)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5153)

