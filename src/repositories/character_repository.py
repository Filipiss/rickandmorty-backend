from src.models import db
from src.models.character_model import Character

class CharacterRepository:
  
    def get_character(self, id):
        return db.session.get(Character, id)

    def get_all_characters(self, name, limit, offset):
        query = Character.query
        
        if name:
            query = query.filter(Character.name.ilike(f"%{name}%"))
        
        total = query.count() 

        results = query.limit(limit).offset(offset).all()

        return results, total
    