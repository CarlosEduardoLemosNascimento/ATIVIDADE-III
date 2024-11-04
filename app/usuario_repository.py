from sqlalchemy.orm import Session
from models import Usuario
from database import get_db

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session

    def criar(self, nome: str, email: str, senha: str):
        usuario = Usuario(nome=nome, email=email, senha=senha)
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
        return usuario

    def listar_todos(self):
        return self.session.query(Usuario).all()

    def consultar(self, user_id: int):
        return self.session.query(Usuario).filter(Usuario.id == user_id).first()

    def atualizar(self, user_id: int, nome: str, email: str, senha: str):
        usuario = self.consultar(user_id)
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
            self.session.commit()
            return usuario
        return None

    def excluir(self, user_id: int):
        usuario = self.consultar(user_id)
        if usuario:
            self.session.delete(usuario)
            self.session.commit()
            return usuario
        return None
