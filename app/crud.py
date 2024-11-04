from models import Usuario
from database import db

def adicionar_usuario(nome, email):
    """Adicionar um novo usuário ao banco de dados."""
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

def listar_usuarios():
    """Retorna todos os usuários cadastrados."""
    return Usuario.query.all()

def pesquisar_usuario(user_id):
    """Retorna um usuário específico pelo ID."""
    return Usuario.query.get(user_id)

def atualizar_usuario(user_id, nome, email):
    """Atualiza os dados de um usuário existente."""
    usuario = Usuario.query.get(user_id)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        db.session.commit()
        return usuario
    return None

def excluir_usuario(user_id):
    """Exclui um usuário do banco de dados."""
    usuario = Usuario.query.get(user_id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False
