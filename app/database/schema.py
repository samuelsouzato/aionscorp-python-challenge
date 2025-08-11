from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ContatoBase(BaseModel):
    """
    Campos básicos de um contato (entrada).
    """
    nome: str
    telefone: str
    email: str
    tags:str

class ContatoCreate(ContatoBase):
    """
    Schema para criação de contato 
    """
    pass

class ContatoResponse(ContatoBase):
    """
    Schema para resposta de dados do contato
    """
    id: int
    model_config = ConfigDict(from_attributes=True)


class ContatoMensagemResponse(BaseModel):
    """
    Schema para respostas que retornam uma mensagem + o contato criado/atualizado.
    Ex.: {"mensagem": "Contato criado com sucesso!", "contato": {...}}
    """
    mensagem: str
    contato: ContatoResponse

    model_config = ConfigDict(from_attributes=True)