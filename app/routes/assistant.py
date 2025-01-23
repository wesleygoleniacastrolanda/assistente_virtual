from fastapi import APIRouter
from app.models.request_models import TextRequest
from app.services.assistant_service import process_text

router = APIRouter()

@router.post("/process")
def process_text_endpoint(request: TextRequest):
    return process_text(request.text)