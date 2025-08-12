from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.models import Contato
from app.database.database import pegar_db
from app.database.schema import ContatoCreate, ContatoResponse, ContatoMensagemResponse
from app.controllers.contato_controller import (
    create,
    find_id,
    find_tags,
    update,
    delete
)

router = APIRouter(prefix="/contatos", tags=["Contatos"])

@router.post("/contato_create", response_model=ContatoMensagemResponse, summary="Criar novo contato")
async def criar_contato_route(contato: ContatoCreate, db: Session = Depends(pegar_db)):
    """
    Rota para criar um contato. Retorna mensagem + contato criado.
    """
    return create(db, contato)


@router.get("/contato_list", response_model=List[ContatoResponse], summary="Listar contatos(todos ou por tags)")
async def listar_contatos_route(
    tag: Optional[str] = Query(None, description="Filtrar por tag"),
    page: int = Query(1, ge=1, description="Número da página"),
    per_page: int = Query(10, ge=1, le=100, description="Quantidade de itens por página"),
    db: Session = Depends(pegar_db)
    ):
    """
    Rota para listar contatos, com suporte a filtro por tag e paginação.
    """
    if tag:
        tags_list = [tag.strip().lower() for tag in tag.split(",")]
        return find_tags(tags_list, db, page, per_page)
    else:
        offset = (page - 1) * per_page
        contatos = db.query(Contato).offset(offset).limit(per_page).all()
        return [ContatoResponse.model_validate(item) for item in contatos]

@router.get("/{contato_id}", response_model=ContatoResponse, summary="Buscar contato por ID")
async def buscar_contato_route(contato_id: int, db: Session = Depends(pegar_db)):
    """
    Rota para buscar um contato por ID.
    """
    return find_id(db, contato_id)


@router.put("/{contato_id}", response_model=ContatoMensagemResponse, summary="Atualizar contato")
async def atualizar_contato_route(contato_id: int, contato: ContatoCreate, db: Session = Depends(pegar_db)):
    """
    Rota para atualizar um contato e retornar mensagem + contato atualizado.
    """
    return update(db, contato_id, contato)


@router.delete("/{contato_id}", summary="Excluir contato")
async def excluir_contato_route(contato_id: int, db: Session = Depends(pegar_db)):
    """
    Rota para excluir contato (retorna mensagem de sucesso).
    """
    return delete(db, contato_id)