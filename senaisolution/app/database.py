from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração da URL de conexão ao banco de dados MySQL
DATABASE_URL = "mysql+mysqlconnector://user:user_password@db/meu_banco"

# Criação do motor e da sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
