from sqlalchemy.orm import Session
from .models import Usuario

def adicionar_usuario(db: Session, nome: str, email: str):
    usuario = Usuario(nome=nome, email=email)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def pesquisar_usuario(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

def atualizar_usuario(db: Session, user_id: int, nome: str, email: str):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if usuario:
        usuario.nome = nome
        usuario.email = email
        db.commit()
        return usuario
    return None

def excluir_usuario(db: Session, user_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
        return usuario
    return None
