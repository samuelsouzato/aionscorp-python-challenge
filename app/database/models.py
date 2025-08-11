from sqlalchemy import Column, String, Integer
from app.database.database import Base

# classe/tebela do banco de dados
class Contato(Base):
    __tablename__ = "contatos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    email = Column("email", String, nullable=False)
    tags = Column("tags", String, nullable=True)

    def __init__(self, nome, telefone, email, tags):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tags = tags
           
