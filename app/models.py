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
    # Substitua 'mysql+pymysql://user:password@localhost/meu_banco' pelos seus detalhes de conexão
    engine = create_engine('mysql+pymysql://user:password@localhost/meu_banco')
    Base.metadata.create_all(engine)

def main():
    # Chama a função para criar a tabela
    criar_tabela()
    

    print("Tabela criada com sucesso!")