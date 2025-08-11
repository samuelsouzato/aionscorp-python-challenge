from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# conexão do banco de dados
db= create_engine("sqlite:///banco.db")

# base do banco de dados
Base = declarative_base()

# Criar fábrica de sessões
session= sessionmaker(bind=db)

def pegar_db():
    """
    Retorna uma sessão de banco de dados para ser usada em requests.
    Fecha automaticamente após o uso.
    """
    db = session()
    try:
        yield db
        # independente do erro fecha
    finally: 
        db.close()
