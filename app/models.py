# models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(100), nullable=False)

def criar_tabela():
    # Cria a tabela no banco de dados
    engine = create_engine('mysql+pymysql://user:user_password@localhost/meu_banco')
    Base.metadata.create_all(engine)
