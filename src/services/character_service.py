from src.repositories.character_repository import CharacterRepository
from src.models.character_model import character_output_get_all, character_output_get_by_id, character_meta_output
from math import ceil


class CharacterService:

    def __init__(self):
        self.character_repository = CharacterRepository()
    
    def get_all_characters(self, name, page):
        limit = 20
        page = int(page) if page and page.isdecimal() else 1
        offset = (page - 1) * limit

        results, total = self.character_repository.get_all_characters(
            name=name,
            limit=limit,
            offset=offset
        )

        total_pages = ceil(total / limit) if total > 0 else 1

        pagination_data = {
            "current_page": page,
            "per_page": limit,
            "total_results": total,
            "total_pages": total_pages
        }

        return {
            "characters": character_output_get_all.dump(results, many=True),
            "meta": character_meta_output.dump(pagination_data)
        }
    
    
    def get_character(self, id):
        character = self.character_repository.get_character(id)

        if not character:
            return None 

        return character_output_get_by_id.dump(character)