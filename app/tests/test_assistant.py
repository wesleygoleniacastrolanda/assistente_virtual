from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_text():
    response = client.post("/assistant/process", json={"text": "Qual o status do pedido 123456?"})
    assert response.status_code == 200
    assert response.json()["intention"] == "consulta_pedido"
    assert response.json()["status"] == "em preparo"

def test_general_question():
    response = client.post("/assistant/process", json={"text": "Quem é você?"})
    assert response.status_code == 200
    assert response.json()["intention"] == "informacao_geral"
    assert response.json()["answer"] == "Eu sou um assistente virtual desenvolvido para ajudá-lo a responder perguntas!"
