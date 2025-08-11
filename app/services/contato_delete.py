
from sqlalchemy.orm import Session
from app.database.models import Contato

def delete_contato(db: Session, contato_id: int):
    """
    Remove um contato pelo ID.
    """
    contato_db = db.query(Contato).filter(Contato.id == contato_id).first()
    if not contato_db:
        return None

    db.delete(contato_db)
    db.commit()
    return contato_db