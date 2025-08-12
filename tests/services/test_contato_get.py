import pytest
from unittest.mock import MagicMock
from app.services import contato_get
from app.database import models

def test_contato_find_all():
    """
    Testa a listagem de todos os contatos.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy
    contatos_fakes = contatos_fakes = [MagicMock(id=1), MagicMock(id=2)]  # cria dois objetos falsos simulando contatos com atributo 'id'
    mock_db.query().offset().limit().all.return_value = contatos_fakes  # retorna lista

    result = contato_get.contato_find_all(mock_db, offset=0, limit=10)

    assert result == contatos_fakes

def test_contato_find_tags():
    """
    Testa busca de contatos por tags.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy

    # cria dois contatos falsos simulando que possuem a tag "casa"
    contato1 = MagicMock()
    contato1.tags = ["casa"]
    contato2 = MagicMock()
    contato2.tags = ["casa"]
    contatos_fakes = [contato1, contato2]

    # configura o mock do banco para retornar a lista fake
    mock_db.query().filter().offset().limit().all.return_value = contatos_fakes

    # chama a função de busca com tags simuladas
    result = contato_get.contato_find_tags(
        mock_db, contato_tags=["casa"], offset=0, limit=10
    )

    # verifica se o retorno é o que esperamos
    assert result == contatos_fakes
  
def test_contato_find_id_existente():
    """
    Testa busca de contato por ID existente.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy
    contato_falso = models.Contato(nome="juju", telefone="12345", email="juju", tags="casa")
    contato_falso.id = 1
    mock_db.query().filter().first.return_value = contato_falso  # retorna contato

    result = contato_get.contato_find_id(mock_db, 1)

    assert result == contato_falso

def test_contato_find_id_inexistente():
    """
    Testa busca de contato por ID inexistente.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy
    mock_db.query().filter().first.return_value = None  # nenhum contato encontrado

    result = contato_get.contato_find_id(mock_db, 999)

    assert result is None

