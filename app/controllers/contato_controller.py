from fastapi import HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.database.models import Contato
from app.database.schema import ContatoCreate, ContatoResponse, ContatoMensagemResponse
from app.services.contato_create import create_contato
from app.services.contato_get import contato_find_all, contato_find_id, contato_find_tags
from app.services.contato_update import update_contato
from app.services.contato_delete import delete_contato
from sqlalchemy import or_

def create(db: Session, contato: ContatoCreate) -> ContatoMensagemResponse:
    """
    Controller para criar um contato.
    - Verifica se já existe um contato com mesmo nome ou telefone.
    - Em caso afirmativo, lança HTTPException 400.
    - Caso contrário, chama o service create_contato e retorna mensagem + contato.
    """
    existente = db.query(Contato).filter(
        or_(
            Contato.nome == contato.nome,
            Contato.telefone == contato.telefone
        )
    ).first()

    if existente:
        # Mensagem clara para o cliente
        raise HTTPException(status_code=400,
                            detail="Já existe um contato com este nome ou telefone.")

    novo = create_contato(db, contato)
    # Monta resposta usando schemas 
    return ContatoMensagemResponse(mensagem="Contato criado com sucesso!",
                                  contato=ContatoResponse.model_validate(novo))


def find_all(db: Session, page: int, per_page: int) -> List[ContatoResponse]:
    """
    Controller para listar todos os contatos.
    Retorna lista de ContatoResponse.
    """
    offset = (page - 1) * per_page
    contatos = db.query(Contato).limit(per_page).offset(offset).all()
    # Model_validate aceita ORM objects por from_attributes
    return [ContatoResponse.model_validate(item) for item in contatos]

def find_tags(contato_tags: str, db: Session, page: int, per_page: int) -> List[ContatoResponse]:
    """
    Controller para listar contatos por tags.
    Retorna lista de ContatoResponse.
    """
    offset = (page - 1) * per_page
    contatos = contato_find_tags(db, contato_tags, offset, per_page)
    if not contatos:
        raise HTTPException(status_code=404, detail="Não existe nenhum contato com esta tag nesta página!")
    # Model_validate aceita ORM objects por from_attributes
    return [ContatoResponse.model_validate(item) for item in contatos] 


def find_id(db: Session, contato_id: int) -> ContatoResponse:
    """
    Controller para buscar um contato por ID.
    Lança 404 se não encontrado.
    """
    contato = contato_find_id(db, contato_id)
    if not contato:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return ContatoResponse.model_validate(contato)


def update(db: Session, contato_id: int, contato: ContatoCreate) -> ContatoMensagemResponse:
    """
    Controller para atualizar um contato.
    - Usa o service de update; se não encontrado, lança 404.
    - Retorna mensagem + contato atualizado.
    """
    atualizado = update_contato(db, contato_id, contato)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Contato não encontrado")

    return ContatoMensagemResponse(mensagem="Contato atualizado com sucesso!",
                                   contato=ContatoResponse.model_validate(atualizado))


def delete(db: Session, contato_id: int):
    """
    Controller para deletar um contato.
    - Retorna mensagem de sucesso ou lança 404 se não encontrado.
    """
    deletado = delete_contato(db, contato_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Contato não encontrado")
    return {"mensagem": "Contato removido com sucesso"}