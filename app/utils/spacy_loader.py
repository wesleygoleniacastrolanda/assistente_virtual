import spacy
from app.config import settings

nlp = spacy.load(settings.SPACY_MODEL)