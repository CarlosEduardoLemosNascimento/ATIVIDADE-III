# Dicionário para armazenar usuários
usuarios = {}
proximo_id = 1  # ID inicial para o próximo usuário

def adicionar_usuario(nome, email):
    global proximo_id
    usuarios[proximo_id] = {'nome': nome, 'email': email}
    proximo_id += 1
    print(f"Usuário {nome} adicionado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("Usuários cadastrados:")
    for id, info in usuarios.items():
        print(f"ID: {id}, Nome: {info['nome']}, Email: {info['email']}")

def pesquisar_usuario(user_id):
    usuario = usuarios.get(user_id)
    if usuario:
        print(f"Usuário encontrado: ID: {user_id}, Nome: {usuario['nome']}, Email: {usuario['email']}")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario(user_id, nome, email):
    usuario = usuarios.get(user_id)
    if usuario:
        usuario['nome'] = nome
        usuario['email'] = email
        print(f"Usuário ID {user_id} atualizado com sucesso!")
    else:
        print("Usuário não encontrado.")

def excluir_usuario(user_id):
    if user_id in usuarios:
        del usuarios[user_id]
        print(f"Usuário ID {user_id} excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n== MENU ==")
        print("1 - Adicionar Usuário")
        print("2 - Listar Usuários")
        print("3 - Pesquisar Usuário")
        print("4 - Atualizar Usuário")
        print("5 - Excluir Usuário")
        print("0 - Sair")
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            adicionar_usuario(nome, email)
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            user_id = int(input("Digite o ID do usuário a ser pesquisado: "))
            pesquisar_usuario(user_id)
        elif opcao == '4':
            user_id = int(input("Digite o ID do usuário a ser atualizado: "))
            nome = input("Digite o novo nome do usuário: ")
            email = input("Digite o novo email do usuário: ")
            atualizar_usuario(user_id, nome, email)
        elif opcao == '5':
            user_id = int(input("Digite o ID do usuário a ser excluído: "))
            excluir_usuario(user_id)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()
