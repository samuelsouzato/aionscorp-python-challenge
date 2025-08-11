from sqlalchemy.orm import Session
from app.database.models import Contato
from app.database.schema import ContatoCreate

def update_contato(db: Session, contato_id: int, contato: ContatoCreate):
    """
    Atualiza um contato existente pelo ID.
    """
    contato_db = db.query(Contato).filter(Contato.id == contato_id).first()
    if not contato_db:
        return None

    contato_db.nome = contato.nome
    contato_db.telefone = contato.telefone
    contato_db.email = contato.email
    contato_db.tags = contato.tags

    db.commit()
    db.refresh(contato_db)
    return contato_db