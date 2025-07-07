from flask import Flask, render_template, request, redirect, url_for
from models import db, Task

app = Flask(__name__)
# Configura o caminho do banco de dados SQLite.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Inicia a conexão do banco de dados com o app Flask.
db.init_app(app)

# Rota principal que exibe a lista de animais.
@app.route('/')
def index():
    # Pega o bioma que o usuário selecionou no filtro da URL.
    search_biome = request.args.get('biome', None, type=str)

    # Define a paginação para exibir 10 itens por página.
    page = request.args.get('page', 1, type=int)
    per_page = 10

    query = Task.query

    # Se um bioma foi escolhido, adiciona o filtro na consulta.
    if search_biome and search_biome.strip():
        query = query.filter(Task.bioma.ilike(f'%{search_biome}%'))

    # Busca todos os biomas únicos no banco para o menu de filtro.
    all_biomas_from_db = db.session.query(Task.bioma).distinct().all()
    
    # Processa e limpa a lista de biomas para não ter repetições.
    unique_biomes = set()
    for bioma_tuple in all_biomas_from_db:
        bioma_string = bioma_tuple[0]
        individual_biomes = [b.strip() for b in bioma_string.split(',')]
        unique_biomes.update(individual_biomes)
    
    # Coloca os biomas em ordem alfabética para o menu.
    sorted_unique_biomes = sorted(list(unique_biomes))

    # Executa a consulta com a paginação.
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    tasks = pagination.items

    # Envia os dados dos animais e da paginação para o HTML.
    return render_template(
        "index.html", 
        tasks=tasks, 
        pagination=pagination,
        all_biomes=sorted_unique_biomes,
        search_biome=search_biome
    )

# Rota para criar um novo animal no banco de dados.
@app.route("/create", methods=["POST"])
def create_task():
    # Pega os dados enviados pelo formulário de criação.
    nome = request.form["nome"]
    nome_cientifico = request.form["nome_cientifico"]
    status = request.form["status"]
    regiao = request.form["regiao"]
    bioma = request.form["bioma"]

    # Cria um novo objeto 'Task' (animal) com esses dados.
    new_task = Task(
        nome=nome,
        nome_cientifico=nome_cientifico,
        status=status,
        regiao=regiao,
        bioma=bioma
    )

    # Tenta adicionar o novo animal ao banco de dados.
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Erro ao salvar no banco: {e}"

    # Redireciona o usuário de volta para a página inicial.
    return redirect(url_for('index'))

# Rota para deletar um animal específico pelo seu ID.
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    # Busca o animal pelo ID ou retorna um erro 404 se não encontrar.
    task = Task.query.get_or_404(task_id)
    
    # Tenta remover o animal do banco de dados.
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Erro ao deletar do banco: {e}"
        
    # Redireciona o usuário de volta para a página inicial.
    return redirect(url_for('index'))

# Rota para abrir a página de edição de um animal.
@app.route("/edit/<int:task_id>")
def edit_task_page(task_id):
    # Busca o animal pelo ID e o envia para a página de edição.
    task = Task.query.get_or_404(task_id)
    return render_template("edit.html", task=task)

# Rota para atualizar os dados de um animal no banco.
@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    # Busca o animal que será atualizado.
    task = Task.query.get_or_404(task_id)
    
    if task:
        # Tenta atualizar os dados do animal com as informações do formulário.
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
            
    # Redireciona o usuário de volta para a página inicial.
    return redirect(url_for('index'))

# Bloco que executa a aplicação.
if __name__ == "__main__":
    # Garante que as tabelas do banco de dados sejam criadas antes de rodar.
    with app.app_context():
        db.create_all()

    # Inicia o servidor Flask em modo de depuração.
    app.run(debug=True, port=5153)