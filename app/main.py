# main.py
from app.usuario_service import UsuarioService
from app.usuario_repository import UsuarioRepository
from app.database import get_db
from app.models import criar_tabela

def main():
    # Cria a tabela no banco se ela ainda não existir
    criar_tabela()

    service = UsuarioService()
    
    while True:
        print(f"\n== MENU PRINCIPAL ==")
        print(f"1 - Cadastrar Usuário")
        print(f"2 - Pesquisar um Usuário")
        print(f"3 - Atualizar dados de um Usuário")
        print(f"4 - Excluir um Usuário")
        print(f"5 - Exibir todos os Usuários cadastrados")
        print(f"0 - Sair")
        
        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            with get_db() as db_session:
                repository = UsuarioRepository(db_session)
                service.set_repository(repository)
                cadastrar_usuario(service)
        elif opcao == "2":
            with get_db() as db_session:
                repository = UsuarioRepository(db_session)
                service.set_repository(repository)
                pesquisar_usuario(service)
        elif opcao == "3":
            with get_db() as db_session:
                repository = UsuarioRepository(db_session)
                service.set_repository(repository)
                atualizar_usuario(service)
        elif opcao == "4":
            with get_db() as db_session:
                repository = UsuarioRepository(db_session)
                service.set_repository(repository)
                excluir_usuario(service)
        elif opcao == "5":
            with get_db() as db_session:
                repository = UsuarioRepository(db_session)
                service.set_repository(repository)
                listar_usuarios(service)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_usuario(service):
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    service.criar_usuario(nome, email, senha)
    print("Usuário cadastrado com sucesso!")

def pesquisar_usuario(service):
    user_id = int(input("Digite o ID do usuário: "))
    usuario = service.consultar_usuario(user_id)
    if usuario:
        print(f"Nome: {usuario.nome}, Email: {usuario.email}")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario(service):
    user_id = int(input("Digite o ID do usuário a ser atualizado: "))
    nome = input("Novo nome: ")
    email = input("Novo e-mail: ")
    senha = input("Nova senha: ")
    service.atualizar_usuario(user_id, nome, email, senha)
    print("Usuário atualizado com sucesso!")

def excluir_usuario(service):
    user_id = int(input("Digite o ID do usuário a ser excluído: "))
    service.excluir_usuario(user_id)
    print("Usuário excluído com sucesso!")

def listar_usuarios(service):
    usuarios = service.listar_todos_usuario()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

if __name__ == "__main__":
    main()
