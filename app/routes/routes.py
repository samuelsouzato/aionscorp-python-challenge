from fastapi import APIRouter, HTTPException
from app.models.contato import Contato,db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

routes = APIRouter(prefix="/contatos", tags=["contatos"])

@routes.get("/")
async def contatos():
    """
    Rota padrão
    """
    return {"mensagem": "Você acessou a rota de contatos"}

@routes.post("/contato")
async def criar_contato(nome: str,telefone: str, email: str, tags: str):
    # Abrindo sessão conectada ao banco (engine)
    Session= sessionmaker(bind=db)
    session = Session()
    # Verifica se já existe um contato com o mesmo nome ou telefone
    contato = session.query(Contato).filter(or_(Contato.nome==nome, Contato.telefone==telefone)).first()
    if contato:
        # já existe um contato com este nome ou telefone
        return HTTPException(status_code=400, detail="Nome ou telefone já cadastrado")
    else:
        novo_contato = Contato(nome, telefone, email, tags)
        session.add(novo_contato)
        session.commit() # salva todas alterações no banco de dados
        return {"mensagem": "Contato criado com sucesso!"}