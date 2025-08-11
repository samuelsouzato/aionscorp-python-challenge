from sqlalchemy.orm import Session
from app.database.models import Contato
from sqlalchemy import or_

def contato_find_all(db: Session, offset: int, limit: int):
    """
    Retorna todos os contatos cadastrados.
    """
    return db.query(Contato).offset(offset).limit(limit).all()

def contato_find_tags(db: Session, contato_tags: str,  offset: int, limit: int):
    """
    Retorna contatos que contenham pelo menos uma das tags informadas (parcial e case-insensitive).
    """
    # Criar lista de condições com LIKE para cada tag, usando lower para case-insensitive
    conditions = [Contato.tags.ilike(f"%{tag}%") for tag in contato_tags]

    return db.query(Contato)\
        .filter(or_(*conditions))\
        .offset(offset)\
        .limit(limit)\
        .all()

def contato_find_id(db: Session, contato_id: int):
    """
    Retorna um contato específico pelo ID.
    """
    return db.query(Contato).filter(Contato.id == contato_id).first()