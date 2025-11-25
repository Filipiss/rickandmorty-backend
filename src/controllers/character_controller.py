from flask import jsonify
from src.services.character_service import CharacterService
from marshmallow.exceptions import ValidationError 

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_character(self, id):
        try:
            id = int(id)

            data = self.character_service.get_character(id)

            if data is None:
                return jsonify({"error": "Character not found"}), 404

            return jsonify(data), 200

        except ValidationError:
            return jsonify({"error": "Invalid ID"}), 400

        except Exception as e:
            print("ERRO NA CONTROLLER:", e)
            return jsonify({"error": "server error"}), 500
