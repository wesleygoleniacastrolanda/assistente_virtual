from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.nlp import detect_intent

router = APIRouter(prefix="/ask", tags=["Assistente Virtual"])

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    intent: str
    answer: str

@router.post("/", response_model=QuestionResponse)
def ask_question(payload: QuestionRequest):
    """
    Endpoint para interpretar a intenção da pergunta e retornar uma resposta.
    """
    intent = detect_intent(payload.question)

    # Simulação de respostas com base na intenção detectada
    if intent == "consultar_status_pedido":
        answer = "O pedido 12345 está em processamento."
    else:
        answer = "Desculpe, não entendi sua pergunta."

    return {"intent": intent, "answer": answer}
