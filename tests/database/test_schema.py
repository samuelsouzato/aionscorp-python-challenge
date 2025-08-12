import pytest
from pydantic import ValidationError
from app.database import schema

def test_schema_contato_criacao_invalido():
    """
    Testa a validação do schema ContactCreate com dados inválidos.

    Cenário:
    - Envia nome vazio, e-mail inválido e telefone não numérico.
    - Espera que o Pydantic levante ValidationError.
    """
    with pytest.raises(ValidationError):
        schema.ContatoCreate(name="", email="email_errado", phone="abc")
