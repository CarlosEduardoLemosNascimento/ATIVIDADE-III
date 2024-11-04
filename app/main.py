from sqlalchemy.orm import Session
from .database import SessionLocal
from .crud import adicionar_usuario, listar_usuarios, pesquisar_usuario, atualizar_usuario, excluir_usuario

def menu():
    db: Session = SessionLocal()

    while True:
        print("\n== SENAI SOLUTION ==")
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
            adicionar_usuario(db, nome, email)
            print("Usuário adicionado com sucesso!")
        elif opcao == '2':
            user_id = int(input("Digite o ID do usuário a ser pesquisado: "))
            usuario = pesquisar_usuario(db, user_id)
            if usuario:
                print(f"Usuário encontrado: ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
            else:
                print("Usuário não encontrado.")
        elif opcao == '3':
            user_id = int(input("Digite o ID do usuário a ser atualizado: "))
            nome = input("Digite o novo nome do usuário: ")
            email = input("Digite o novo email do usuário: ")
            usuario = atualizar_usuario(db, user_id, nome, email)
            if usuario:
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado.")
        elif opcao == '4':
            user_id = int(input("Digite o ID do usuário a ser excluído: "))
            usuario = excluir_usuario(db, user_id)
            if usuario:
                print("Usuário excluído com sucesso!")
            else:
                print("Usuário não encontrado.")
        elif opcao == '5':
            usuarios = listar_usuarios(db)
            if usuarios:
                print("Usuários cadastrados:")
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")
            else:
                print("Nenhum usuário cadastrado.")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
