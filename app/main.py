from services.usuario_service import UsuarioService
from database import get_db

def main():
    service = UsuarioService()

    while True:
        print(f"\n== MENU PRINCIPAL ==")
        print(f"1 - Adicionar Usuário")
        print(f"2 - Pesquisar Usuário")
        print(f"3 - Atualizar Dados de Usuário")
        print(f"4 - Excluir Usuário")
        print(f"5 - Exibir Todos os Usuários Cadastrados")
        print(f"0 - Sair")
        opcao = input("Informe a opção desejada: ")

        with get_db() as session:
            service.set_repository(session)

            if opcao == '1':
                nome = input("Digite seu nome: ")
                email = input("Digite seu e-mail: ")
                senha = input("Digite sua senha: ")
                service.criar_usuario(nome=nome, email=email, senha=senha)
                print("Usuário cadastrado com sucesso!")

            elif opcao == '2':
                user_id = int(input("Digite o ID do usuário a ser pesquisado: "))
                usuario = service.consultar_usuario(user_id)
                if usuario:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                else:
                    print("Usuário não encontrado.")

            elif opcao == '3':
                user_id = int(input("Digite o ID do usuário a ser atualizado: "))
                nome = input("Digite o novo nome: ")
                email = input("Digite o novo e-mail: ")
                senha = input("Digite a nova senha: ")
                service.atualizar_usuario(user_id=user_id, nome=nome, email=email, senha=senha)
                print("Usuário atualizado com sucesso!")

            elif opcao == '4':
                user_id = int(input("Digite o ID do usuário a ser excluído: "))
                service.excluir_usuario(user_id)
                print("Usuário excluído com sucesso!")

            elif opcao == '5':
                print("\nListando usuários cadastrados:")
                usuarios = service.listar_todos_usuario()
                for usuario in usuarios:
                    print(f"ID: {usuario.id}, Nome: {usuario.nome}, Email: {usuario.email}")

            elif opcao == '0':
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
