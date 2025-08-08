from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import JSON

# conexão do banco de dados
db= create_engine("sqlite:///banco.db")

# base do banco de dados
Base = declarative_base()

# classe/tebela do banco de dados
class Contato(Base):
    __tablename__ = "contatos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    email = Column("email", String, nullable=False, unique=True)
    tags = Column("tags", JSON, nullable=True)

    def __init__(self, nome, telefone, email, tags):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tags = tags
           