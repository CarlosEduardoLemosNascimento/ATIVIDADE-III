from sqlalchemy.orm import Session
from app.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repository = None

    def set_repository(self, session: Session):
        self.repository = UsuarioRepository(session)

    def validar_dados(self, nome: str, email: str, senha: str):
        if not nome or not email or not senha:
            raise ValueError("Nome, email e senha são obrigatórios.")
        if "@" not in email:
            raise ValueError("Email inválido.")
    
    def criar_usuario(self, nome: str, email: str, senha: str):
        self.validar_dados(nome, email, senha)
        return self.repository.criar(nome, email, senha)

    def listar_todos_usuario(self):
        return self.repository.listar_todos()

    def consultar_usuario(self, user_id: int):
        return self.repository.consultar(user_id)

    def atualizar_usuario(self, user_id: int, nome: str, email: str, senha: str):
        self.validar_dados(nome, email, senha)
        return self.repository.atualizar(user_id, nome, email, senha)

    def excluir_usuario(self, user_id: int):
        return self.repository.excluir(user_id)
