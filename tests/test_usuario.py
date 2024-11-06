import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Usuario
from app.database import DATABASE_URL

@pytest.fixture(scope='module')
def test_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)  # Cria as tabelas para o teste
    connection = engine.connect()
    transaction = connection.begin()
    
    yield connection

    transaction.rollback()
    connection.close()
    Base.metadata.drop_all(engine)

@pytest.fixture
def session(test_db):
    """Cria uma sessão para os testes."""
    SessionLocal = sessionmaker(bind=test_db)
    session = SessionLocal()
    yield session
    session.close()

def test_criar_usuario(session):
    from app.usuario_repository import UsuarioRepository

    repo = UsuarioRepository(session)
    usuario = repo.criar("Teste", "teste@exemplo.com", "senha123")

    assert usuario.id is not None
    assert usuario.nome == "Teste"
    assert usuario.email == "teste@exemplo.com"

def test_listar_usuarios(session):
    from app.usuario_repository import UsuarioRepository

    repo = UsuarioRepository(session)
    repo.criar("Usuario 1", "user1@exemplo.com", "senha123")
    repo.criar("Usuario 2", "user2@exemplo.com", "senha123")

    usuarios = repo.listar_todos()
    assert len(usuarios) >= 2

def test_atualizar_usuario(session):
    from app.usuario_repository import UsuarioRepository

    repo = UsuarioRepository(session)
    usuario = repo.criar("Atualizar", "atualizar@exemplo.com", "senha123")
    
    repo.atualizar(usuario.id, "Atualizado", "atualizado@exemplo.com", "nova_senha")
    usuario_atualizado = repo.consultar(usuario.id)

    assert usuario_atualizado.nome == "Atualizado"
    assert usuario_atualizado.email == "atualizado@exemplo.com"

def test_excluir_usuario(session):
    from app.usuario_repository import UsuarioRepository

    repo = UsuarioRepository(session)
    usuario = repo.criar("Excluir", "excluir@exemplo.com", "senha123")

    repo.excluir(usuario.id)
    usuario_excluido = repo.consultar(usuario.id)

    assert usuario_excluido is None
