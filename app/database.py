from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com o Banco de Dados
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço/caminho para conexão com o banco de dados MySQL
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Gerenciando a sessão
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()  # Se der certo, faz commit.
    except Exception as erro:
        db.rollback()  # Se der erro, desfaz a operação.
        raise erro  # Lança a exceção de erro
    finally:
        db.close()  # Fechando a conexão
