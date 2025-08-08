from fastapi import APIRouter

routes = APIRouter(prefix="/contatos", tags=["contatos"])

@routes.get("/")
async def contatos():
    """
    Rota padrão
    """
    return {"mensagem": "Você acessou a rota de contatos"}