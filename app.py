# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    pagination = Task.query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items
    return render_template("index.html", tasks=tasks, pagination=pagination)

@app.route("/create", methods=["POST"])
def create_task():
    nome = request.form["nome"]
    nome_cientifico = request.form["nome_cientifico"]
    status = request.form["status"]
    regiao = request.form["regiao"]
    bioma = request.form["bioma"]

    new_task = Task(
        nome=nome,
        nome_cientifico=nome_cientifico,
        status=status,
        regiao=regiao,
        bioma=bioma
    )

    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Erro ao salvar no banco: {e}"

    return redirect(url_for('index'))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Erro ao deletar do banco: {e}"
        
    return redirect(url_for('index'))

@app.route("/edit/<int:task_id>")
def edit_task_page(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("edit.html", task=task)

@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if task:
        try:
            task.nome = request.form["nome"]
            task.nome_cientifico = request.form["nome_cientifico"]
            task.status = request.form["status"]
            task.regiao = request.form["regiao"]
            task.bioma = request.form["bioma"]
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Erro ao atualizar no banco: {e}"
            
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5153)