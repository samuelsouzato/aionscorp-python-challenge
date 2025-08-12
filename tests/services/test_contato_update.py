import pytest
from unittest.mock import MagicMock
from app.services import contato_update
from app.database import schema, models

def test_update_contato_existente():
    """
    Testa atualização de contato existente.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy
    contato_falso = models.Contato(nome="jubiscleia", telefone="12345", email="jubiscleia", tags="casa")  # contato fake
    contato_falso.id = 1
    mock_db.query().filter().first.return_value = contato_falso  # retorna contato existente
    contato_data = schema.ContatoCreate(
        nome="jujuba",
        telefone="12345",
        email="juju@email.com",
        tags="casa"
    )

    result = contato_update.update_contato(mock_db, 1, contato_data)

    assert result.nome == "jujuba"
    assert result.email == "juju@email.com"
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(contato_falso)

def test_update_contato_inexistente():
    """
    Testa atualização quando contato não existe.
    """
    mock_db = MagicMock()  # simula sessão do SQLAlchemy
    mock_db.query().filter().first.return_value = None  # nenhum contato encontrado
    contato_data = schema.ContatoCreate(
        nome="aaaaaaa",
        telefone="12345",
        email="aaaaaa@email.com",
        tags="aaaaaaaa"
    )

    result = contato_update.update_contato(mock_db, 999, contato_data)

    assert result is None
    mock_db.commit.assert_not_called()