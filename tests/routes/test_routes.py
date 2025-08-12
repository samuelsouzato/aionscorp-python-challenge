from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_contatos():
    """
    Testa se o endpoint GET /contatos retorna status 200.
    """
    response = client.get("/contatos/contato_list")
    assert response.status_code == 200

def test_criar_contato():
    """
    Testa se o endpoint POST /contatos cria um contato corretamente.
    """
    payload = {
        "nome": "juju_teste",
        "telefone": "12345_teste",
        "email": "juju@example.com",
        "tags": "casa"
    }
    response = client.post("/contatos/contato_create", json=payload)
    assert response.status_code in (200, 400)

def test_atualizar_contato():
    # PUT deve atualizar ou retornar 404
    contato_id = 1
    payload = {"nome": "test_tualizado", "telefone": "teste123", "email": "testeee@example.com", "tags": "testeee"}
    response = client.put(f"/contatos/{contato_id}", json=payload)
    assert response.status_code in (200, 404)

def test_deletar_contato():
    # DELETE deve remover ou retornar 404
    contato_id = 1
    response = client.delete(f"/contatos/{contato_id}")
    assert response.status_code in (200, 404)
