import csv
from app import app, db, Task

# Função para popular o banco de dados com dados de um arquivo CSV.
def seed_database():
    # Entra no contexto da aplicação Flask para poder usar o `db`.
    with app.app_context():
        print("Garantindo que a tabela 'task' exista...")
        # Cria a tabela no banco de dados, se ela ainda não existir.
        db.create_all()
        print("Tabela pronta.")

        print("Limpando dados antigos da tabela...")
        # Deleta todos os registros existentes para evitar duplicatas.
        db.session.query(Task).delete()
        db.session.commit()
        print("Tabela limpa.")

        # Define o caminho do arquivo CSV que contém os dados.
        csv_file_path = 'Fauna Ameaçada.csv' 
        print(f"Iniciando a leitura do arquivo: {csv_file_path}")

        try:
            # Abre o arquivo CSV para leitura.
            with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
               
                # Cria um leitor de CSV, especificando que o delimitador é ';'.
                csv_reader = csv.reader(file, delimiter=';')
                
                # Cria uma lista para armazenar todos os animais antes de salvar.
                animals_to_add = []
                for row in csv_reader:
                    # Pula linhas que possam estar vazias no arquivo.
                    if not row:
                        continue

                    # Mapeia cada coluna da linha do CSV para um campo do modelo Task.
                    new_animal = Task(
                        nome_cientifico=row[0],
                        nome=row[1],
                        status=row[2],
                        regiao=row[3],
                        bioma=row[4]
                    )
                    # Adiciona o novo animal à lista de espera.
                    animals_to_add.append(new_animal)

                # Salva todos os animais da lista no banco de uma só vez.
                db.session.bulk_save_objects(animals_to_add)
                db.session.commit()
                print(f"Banco de dados populado com sucesso! {len(animals_to_add)} animais adicionados.")

        # Trata possíveis erros que possam ocorrer durante o processo.
        except FileNotFoundError:
            print(f"ERRO: O arquivo '{csv_file_path}' não foi encontrado.")
        except IndexError:
            print(f"ERRO: Uma linha no CSV não tem o número esperado de colunas. Verifique o arquivo.")
        except Exception as e:
            db.session.rollback()
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    seed_database()