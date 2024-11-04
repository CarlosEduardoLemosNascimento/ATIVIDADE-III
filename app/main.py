#from app.usuario_service import UsuarioService
#from app.usuario_repository import UsuarioRepository
#from app.database import Session

#def main():
#    session = Session()
#    repository = UsuarioRepository(session)
#    service = UsuarioService()
#    service.set_repository(session)

#    while True:
#        print(f"\n== MENU PRINCIPAL ==")
#        print(f"1 - Cadastrar Usuário")
#        print(f"2 - Pesquisar um Usuário")
#        print(f"3 - Atualizar dados de um Usuário")
#        print(f"4 - Excluir um Usuário")
#        print(f"5 - Exibir todos os Usuários cadastrados")
#        print(f"0 - Sair")
        
#        opcao = input("Informe a opção desejada: ")

#        if opcao == "1":
#            cadastrar_usuario(service)
#        elif opcao == "2":
#            pesquisar_usuario(service)
#        elif opcao == "3":
#            atualizar_usuario(service)
#        elif opcao == "4":
#            excluir_usuario(service)
#        elif opcao == "5":
#            listar_usuarios(service)
#        elif opcao == "0":
#            break
#        else:
#            print("Opção inválida. Tente novamente.")

#def cadastrar_usuario(service):
#    nome = input("Digite seu nome: ")
#    email = input("Digite seu e-mail: ")
#    senha = input("Digite sua senha: ")
#    service.criar_usuario(nome, email, senha)
#    print("Usuário cadastrado com sucesso!")

#def pesquisar_usuario(service):
#    user_id = int(input("Digite o ID do usuário: "))
#    usuario = service.consultar_usuario(user_id)
#    if usuario:
#        print(f"Nome: {usuario.nome}, Email: {usuario.email}")
#    else:
#        print("Usuário não encontrado.")

#def atualizar_usuario(service):
#    user_id = int(input("Digite o ID do usuário a ser atualizado: "))
#    nome = input("Novo nome: ")
#    email = input("Novo e-mail: ")
#    senha = input("Nova senha: ")
#    service.atualizar_usuario(user_id, nome, email, senha)
#    print("Usuário atualizado com sucesso!")

#def excluir_usuario(service):
#    user_id = int(input("Digite o ID do usuário a ser excluído: "))
#    service.excluir_usuario(user_id)
#    print("Usuário excluído com sucesso!")

#def listar_usuarios(service):
#    usuarios = service.listar_todos_usuario()
#    for usuario in usuarios:
#        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

#if __name__ == "__main__":
#    main()


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Definição da classe que representa a tabela de usuários
class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

# Função para criar a tabela
def criar_tabela():
    # Substitua pelos seus detalhes de conexão
    engine = create_engine('mysql+pymysql://user:password@localhost/meu_banco')
    Base.metadata.create_all(engine)

# Função para cadastrar um usuário
def cadastrar_usuario(session, nome, email, senha):
    novo_usuario = Usuario(nome=nome, email=email, senha=senha)
    session.add(novo_usuario)
    session.commit()
    print("Usuário cadastrado com sucesso!")

# Função para exibir o menu
def exibir_menu():
    print("== MENU PRINCIPAL ==")
    print("1 - Cadastrar Usuário")
    print("2 - Pesquisar um Usuário")
    print("3 - Atualizar dados de um Usuário")
    print("4 - Excluir um Usuário")
    print("5 - Exibir todos os Usuários cadastrados")
    print("0 - Sair")

# Função principal
def main():
    # Cria a tabela ao iniciar o programa
    criar_tabela()
    
    # Cria uma sessão para interagir com o banco de dados
    engine = create_engine('mysql+pymysql://user:password@localhost/meu_banco')
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            # Cadastrar um usuário
            nome = input("Digite seu nome: ")
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            cadastrar_usuario(session, nome, email, senha)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
