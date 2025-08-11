from sqlalchemy.orm import Session
from app.database.models import Contato

def contato_find_all(db: Session):
    """
    Retorna todos os contatos cadastrados.
    """
    return db.query(Contato).all()

def contato_find_id(db: Session, contato_id: int):
    """
    Retorna um contato específico pelo ID.
    """
    return db.query(Contato).filter(Contato.id == contato_id).first()