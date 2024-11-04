from flask import Flask
from database import db
from crud import adicionar_usuario, listar_usuarios, pesquisar_usuario, atualizar_usuario, excluir_usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db/senaisolution'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    """Cria as tabelas no banco de dados antes da primeira requisição."""
    db.create_all()

def menu():
    """Exibe o menu e gerencia as opções do usuário."""
    while True:
        print("\n== SENAI SOLUTION ===")
        print("1 - Adicionar Usuário")
        print("2 - Pesquisar um usuário")
        print("3 - Atualizar dados de um usuário")
        print("4 - Excluir um usuário")
        print("5 - Exibir todos os usuários cadastrados")
        print("0 - Sair")
        
        opcao = input("Informe a opção desejada: ")
        
        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            adicionar_usuario(nome, email)
            print("Usuário adicionado com sucesso!")

        elif opcao == '2':
            user_id = int(input("Digite o ID do usuário: "))
            usuario = pesquisar_usuario(user_id)
            if usuario:
                print(f'Usuário encontrado: {usuario.nome}, {usuario.email}')
            else:
                print("Usuário não encontrado.")

        elif opcao == '3':
            user_id = int(input("Digite o ID do usuário a ser atualizado: "))
            nome = input("Digite o novo nome: ")
            email = input("Digite o novo email: ")
            usuario = atualizar_usuario(user_id, nome, email)
            if usuario:
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado.")

        elif opcao == '4':
            user_id = int(input("Digite o ID do usuário a ser excluído: "))
            if excluir_usuario(user_id):
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")

        elif opcao == '5':
            usuarios = listar_usuarios()
            for usuario in usuarios:
                print(f'{usuario.id}: {usuario.nome}, {usuario.email}')

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    with app.app_context():
        menu()
