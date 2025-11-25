from src.models import db
from src.models.character_model import Character

class CharacterRepository:
  
    def get_character(self, id):
        return Character.query.get(id)


    