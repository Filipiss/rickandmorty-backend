from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output, characters_output
from werkzeug.exceptions import NotFound


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()
    
    def get_all_characters(self, name, page):
        limit = 20
        offset = (int(page) - 1) * limit if page and page.isdecimal else 0
        characters = self.character_repository.get_all_characters(name, limit, offset)
        data = characters_output.dump(characters)
        return data
    
    def get_character(self, id):
        character = self.character_repository.get_character(id)

        if not character:
            raise NotFound

        data = character_output.dump(character)
        return data

