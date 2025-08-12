from unittest.mock import MagicMock
from app.services import contato_delete
from app.database.models import Contato

def test_delete_contato_existente():
    """
    Testa a exclusão de um contato existente.

    Cenário:
    - Banco de dados retorna um contato válido pelo ID.
    - Contato é removido com sucesso.
    """
    mock_db = MagicMock() # simula sessão do SQLAlchemy
    contato_falso = Contato(nome="juju", telefone="12345", email="juju@email.com", tags="casa")
    contato_falso.id = 1
    mock_db.query().filter().first.return_value = contato_falso # retorna contato fake

    resultado = contato_delete.delete_contato(mock_db, 1)

    assert resultado == contato_falso
    mock_db.delete.assert_called_once_with(contato_falso)
    mock_db.commit.assert_called_once()

def test_delete_contato_inexistente():
    """
    Testa a exclusão de um contato que não existe.

    Cenário:
    - Banco de dados retorna None para o ID informado.
    - Função deve retornar None sem chamar commit ou delete.
    """
    mock_db = MagicMock() # simula sessão do SQLAlchemy
    mock_db.query().filter().first.return_value = None # simula um "nenhum contato encontrado"

    resultado = contato_delete.delete_contato(mock_db, 99)

    assert resultado is None
    mock_db.delete.assert_not_called()
    mock_db.commit.assert_not_called()