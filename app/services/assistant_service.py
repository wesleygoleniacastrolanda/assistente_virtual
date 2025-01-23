from app.utils.spacy_loader import nlp
from app.data.intents import pedidos_status, intencoes
from app.data.knowledge_base import knowledge_base


def process_text(text: str):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc]

    # Identificar intenção
    detected_intent = "geral"
    for intent, keywords in intencoes.items():
        if any(keyword in tokens for keyword in keywords):
            detected_intent = intent
            break

    response = {"intention": detected_intent, "tokens": tokens}

    if detected_intent == "consulta_pedido":
        for token in tokens:
            if token in pedidos_status:
                response["status"] = pedidos_status[token]
                break
    if detected_intent == "informacao_geral":
        for token in tokens:
            if token.lower() in knowledge_base:
                response["answer"] = knowledge_base[token.lower()]
                break

    return response