from app.utils.spacy_loader import nlp
from app.data.intents import pedidos_status, intencoes
from app.data.knowledge_base import knowledge_base


def combine_phrases(tokens, phrases):
    combined = []
    skip_next = False
    for i in range(len(tokens) - 1):
        if skip_next:
            skip_next = False
            continue
        phrase = f"{tokens[i]} {tokens[i+1]}"
        if phrase in phrases:
            combined.append(phrase)
            skip_next = True
        else:
            combined.append(tokens[i])
    if not skip_next:
        combined.append(tokens[-1])
    return combined

def process_text(text: str):
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc]
    tokens = combine_phrases(tokens, intencoes["informacao_geral"])

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