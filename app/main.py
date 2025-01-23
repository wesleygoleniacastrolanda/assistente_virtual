from fastapi import FastAPI
from app.routes.assistant import router as assistant_router

def create_app():
    app = FastAPI(title="Virtual Assistant API")
    app.include_router(assistant_router, prefix="/assistant", tags=["Assistant"])
    return app

app = create_app()