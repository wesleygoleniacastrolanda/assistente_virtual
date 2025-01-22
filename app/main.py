from fastapi import FastAPI
from app import routes

app = FastAPI(title="Assistente Virtual com FastAPI e SpaCy")

# Inclui as rotas da API
app.include_router(routes.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo ao Assistente Virtual com FastAPI e SpaCy"}