from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com Banco de Dados
db_user = "user"
db_password = "user_password"
db_host = "db"  # Nome do serviço no docker-compose
db_port = "3306"
db_name = "meu_banco"

# Endereço/caminho para conexão com banco de dados MySQL. "URL"
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados.
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Gerenciando sessão.
@contextmanager
def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
        db_session.commit()  # Se der certo, faz commit.
    except Exception as erro:
        db_session.rollback()  # Se der erro, desfaz a operação.
        raise erro  # Lança a exceção de erro.
    finally:
        db_session.close()  # Fechando a conexão.
