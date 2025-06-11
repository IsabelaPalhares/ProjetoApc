from flask import Flask, render_template, request, redirect
from models import db, Tasks

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    pagination = Tasks.query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items
    return render_template("index.html", tasks=tasks, pagination=pagination)

@app.route("/create", methods=["POST"])
def create_task():
    nome = request.form["nome"]
    nome_cientifico = request.form["nome_cientifico"]
    status = request.form["status"]
    regiao = request.form["regiao"]
    bioma = request.form["bioma"]

    new_task = Tasks(
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

    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5153)

