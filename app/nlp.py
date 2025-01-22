import spacy

# Carrega o modelo SpaCy treinado (substitua pelo caminho do modelo treinado, se necessário)
nlp = spacy.load("pt_core_news_sm")

def detect_intent(question: str) -> str:
    """
    Detecta a intenção a partir de uma pergunta usando o SpaCy.
    """
    doc = nlp(question)
    # Exemplo de lógica para identificar intenção com base em entidades ou palavras-chave
    if "status" in question and "pedido" in question:
        return "consultar_status_pedido"
    return "intencao_desconhecida"
