# Assistente Virtual com FastAPI

## Descrição do Projeto
Este projeto tem como objetivo desenvolver um assistente virtual que seja capaz de entender intenções em perguntas feitas pelos usuários e buscar respostas em um banco de dados, utilizando FastAPI como framework para a construção da API. O sistema é projetado para ser rápido, eficiente e de fácil integração com outras aplicações. Ele utiliza a biblioteca **SpaCy** para Processamento de Linguagem Natural (NLP) e identificação de intenções.

## Tecnologias Utilizadas
- **Python 3.9+:** Linguagem de programação principal.
- **FastAPI:** Framework para construção da API.
- **SpaCy:** Biblioteca de Processamento de Linguagem Natural (NLP) para entender as intenções dos usuários.
- **SAP HANA:** Banco de dados para armazenar e consultar as informações.
- **SQLAlchemy:** Para gerenciar consultas ao banco de dados.
- **Uvicorn:** Servidor ASGI para rodar o projeto.

## Funcionalidades
- Interpretar intenções em perguntas feitas em linguagem natural.
- Traduzir intenções em consultas ao banco de dados.
- Retornar respostas precisas e relevantes.
- Disponibilizar uma API para integração com outros sistemas.

## Como Rodar o Projeto

### Pré-requisitos
- Python 3.9 ou superior instalado.
- Acesso a um banco de dados SAP HANA configurado.
- Gerenciador de pacotes `pip`.
- Modelo de linguagem treinado com SpaCy para detecção de intenções.

### Passos

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/assistente-virtual.git
cd assistente-virtual
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente no arquivo `.env`:**
Crie um arquivo `.env` na raiz do projeto e adicione:
```plaintext
DATABASE_URL=hana+pyhdb://usuario:senha@host:porta
```

5. **Treine ou configure o modelo SpaCy:**
Se necessário, treine um modelo de NLP para detecção de intenções específicas.

6. **Inicie o servidor FastAPI:**
```bash
uvicorn app.main:app --reload
```

7. **Acesse a documentação interativa no navegador:**
Abra [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Estrutura do Projeto
```plaintext
assistente-virtual/
├── app/
│   ├── main.py         # Arquivo principal do FastAPI
│   ├── models.py       # Modelos para o banco de dados
│   ├── routes.py       # Rotas da API
│   ├── services.py     # Lógica para consultas e NLP
│   ├── utils.py        # Funções auxiliares
│   ├── nlp.py          # Módulo de NLP para detecção de intenções
├── tests/
│   ├── test_routes.py  # Testes unitários para as rotas
│   ├── test_services.py# Testes para a lógica do sistema
├── .env                # Configurações sensíveis (não comitar)
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do projeto
```

## Exemplo de Uso

Faça uma requisição para a API com uma pergunta:

- **Endpoint:** `POST /ask`

- **Corpo da Requisição:**
```json
{
  "question": "Qual é o status do pedido 12345?"
}
```

A API processará a intenção da pergunta e retornará uma resposta formatada:

- **Resposta:**
```json
{
  "intent": "consultar_status_pedido",
  "answer": "O pedido 12345 está em processamento."
}
```

## Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:
```bash
git checkout -b minha-feature
```
3. Commit suas alterações:
```bash
git commit -m "Adiciona nova funcionalidade"
```
4. Faça um push para a branch:
```bash
git push origin minha-feature
```
5. Abra um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Para dúvidas ou sugestões, entre em contato:

- **E-mail:** wesleyg@castrolanda.coop.br
- **GitHub:** [wesleygoleniacastrolanda](https://github.com/seu-usuario/assistente-virtual)

