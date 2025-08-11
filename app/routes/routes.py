from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import pegar_db
from app.database.schema import ContatoCreate, ContatoResponse, ContatoMensagemResponse
from app.controllers.contato_controller import (
    create,
    find_all,
    find_id,
    update,
    delete
)

router = APIRouter(prefix="/contatos", tags=["Contatos"])

@router.post("/", response_model=ContatoMensagemResponse, summary="Criar novo contato")
def criar_contato_route(contato: ContatoCreate, db: Session = Depends(pegar_db)):
    """
    Rota para criar um contato. Retorna mensagem + contato criado.
    """
    return create(db, contato)


@router.get("/", response_model=List[ContatoResponse], summary="Listar todos os contatos")
def listar_contatos_route(db: Session = Depends(pegar_db)):
    """
    Rota para listar todos os contatos.
    """
    return find_all(db)


@router.get("/{contato_id}", response_model=ContatoResponse, summary="Buscar contato por ID")
def buscar_contato_route(contato_id: int, db: Session = Depends(pegar_db)):
    """
    Rota para buscar um contato por ID.
    """
    return find_id(db, contato_id)


@router.put("/{contato_id}", response_model=ContatoMensagemResponse, summary="Atualizar contato")
def atualizar_contato_route(contato_id: int, contato: ContatoCreate, db: Session = Depends(pegar_db)):
    """
    Rota para atualizar um contato e retornar mensagem + contato atualizado.
    """
    return update(db, contato_id, contato)


@router.delete("/{contato_id}", summary="Excluir contato")
def excluir_contato_route(contato_id: int, db: Session = Depends(pegar_db)):
    """
    Rota para excluir contato (retorna mensagem de sucesso).
    """
    return delete(db, contato_id)