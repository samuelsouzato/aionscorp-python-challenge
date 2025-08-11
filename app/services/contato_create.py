from sqlalchemy.orm import Session
from app.database.models import Contato
from app.database.schema import ContatoCreate

def create_contato(db: Session, contato: ContatoCreate) -> Contato:
    """
    Cria e persiste um novo contato no banco.

    Args:
        db: sessão do SQLAlchemy
        contato: ContatoCreate (Pydantic) com dados da requisição

    Returns:
        A instância ORM do Contato recém-criado.
    """
    novo_contato = Contato(
        nome=contato.nome,
        telefone=contato.telefone,
        email=contato.email,
        tags=contato.tags
    )
    db.add(novo_contato)
    db.commit()
    db.refresh(novo_contato)
    return novo_contato