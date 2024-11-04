from usuario_repository import UsuarioRepository
from database import get_db

class UsuarioService:
    def __init__(self):
        self.repository = None

    def set_repository(self, session: Session):
        self.repository = UsuarioRepository(session)

    def criar_usuario(self, nome: str, email: str, senha: str):
        return self.repository.criar(nome, email, senha)

    def listar_todos_usuario(self):
        return self.repository.listar_todos()

    def consultar_usuario(self, user_id: int):
        return self.repository.consultar(user_id)

    def atualizar_usuario(self, user_id: int, nome: str, email: str, senha: str):
        return self.repository.atualizar(user_id, nome, email, senha)

    def excluir_usuario(self, user_id: int):
        return self.repository.excluir(user_id)
