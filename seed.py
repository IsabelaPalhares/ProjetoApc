import csv
from app import app, db, Task

def seed_database():
    with app.app_context():
        print("Garantindo que a tabela 'task' exista...")
        db.create_all()
        print("Tabela pronta.")

        print("Limpando dados antigos da tabela...")
        db.session.query(Task).delete()
        db.session.commit()
        print("Tabela limpa.")

        csv_file_path = 'Fauna Ameaçada.csv' 
        print(f"Iniciando a leitura do arquivo: {csv_file_path}")

        try:
            with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
               
                csv_reader = csv.reader(file, delimiter=';')
                
                animals_to_add = []
                for row in csv_reader:
                    if not row:
                        continue

                    # Mapeando os dados pela posição da coluna
                    # coluna 0 -> nome_cientifico
                    # coluna 1 -> nome
                    # coluna 2 -> status
                    # coluna 3 -> regiao
                    # coluna 4 -> bioma
                    new_animal = Task(
                        nome_cientifico=row[0],
                        nome=row[1],
                        status=row[2],
                        regiao=row[3],
                        bioma=row[4]
                    )
                    animals_to_add.append(new_animal)

                db.session.bulk_save_objects(animals_to_add)
                db.session.commit()
                print(f"Banco de dados populado com sucesso! {len(animals_to_add)} animais adicionados.")

        except FileNotFoundError:
            print(f"ERRO: O arquivo '{csv_file_path}' não foi encontrado.")
        except IndexError:
            print(f"ERRO: Uma linha no CSV não tem o número esperado de colunas. Verifique o arquivo.")
        except Exception as e:
            db.session.rollback()
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    seed_database()