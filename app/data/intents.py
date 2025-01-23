pedidos_status = {
    "123456": "em preparo",
    "987654": "entregue",
    "654321": "aguardando pagamento"
}

intencoes = {
    "consulta_pedido": ["pedido","pedidos", "status", "rastrear", "número do pedido"],
    "documentacao_faltante": ["documentação", "faltando", "documentos", "fornecedor"],
    "consulta_pdm": ["pdm", "material", "sistema", "localização"],
    "status_propriedade": ["propriedade", "ativa", "inativa", "cooperado"],
    "informacao_geral": ["quem", "o que", "como", "por que", "onde"],
    "geral": []  # Intenção padrão
}