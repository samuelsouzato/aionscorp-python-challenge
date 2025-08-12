import pytest
from unittest.mock import MagicMock
from app.services import contato_create
from app.database import schema, models

def test_create_contato_sucesso():
    """
    Testa a criação de um novo contato com dados válidos.

    Cenário:
    - Simula um banco de dados vazio.
    - Garante que o contato é criado, commitado e retornado corretamente.
    """
    mock_db = MagicMock() # simula sessão do SQLAlchemy
    contato_data = schema.ContatoCreate(
        nome="juju",
        telefone="123456789",
        email="juju@email.com",
        tags="casa"
    )

    resultado = contato_create.create_contato(mock_db, contato_data)

    assert isinstance(resultado, models.Contato)
    assert resultado.nome == "juju"
    assert resultado.email == "juju@email.com"
    mock_db.add.assert_called_once() # garante que foi adicionado ao DB
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(resultado)