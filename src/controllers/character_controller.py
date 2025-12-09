from flask import jsonify
from src.services.character_service import CharacterService
from werkzeug.exceptions import NotFound
from src.utils.api_response import ApiResponse


class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name, page):
        try:
            result = self.character_service.get_all_characters(name, page)

            return jsonify(ApiResponse.success(
                message="Characters retrieved successfully",
                data=result
            )), 200

        except Exception as e:
            print("ERRO NA CONTROLLER:", e)
            return jsonify(ApiResponse.error("Server error")), 500


    def get_character(self, id):
        try:
            character = self.character_service.get_character(id)

            if character is None:

                raise NotFound("Character not found")

            return jsonify(ApiResponse.success(
                message="Character retrieved successfully",
                data=character
            )), 200
        
        except NotFound as nf:

            return jsonify(ApiResponse.error(str(nf))), 404

        except Exception as e:
            print("ERRO NA CONTROLLER:", e)
            return jsonify(ApiResponse.error("Server error")), 500