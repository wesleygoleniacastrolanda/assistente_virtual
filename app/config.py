import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SPACY_MODEL: str = os.getenv("SPACY_MODEL", "pt_core_news_sm")

settings = Settings()