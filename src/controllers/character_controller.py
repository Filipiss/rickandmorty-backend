from flask import jsonify
from src.services.character_service import CharacterService
from werkzeug.exceptions import NotFound

class CharacterController:

    def __init__(self):
        self.character_service = CharacterService()

    def get_all_characters(self, name, page):
        try:
            data = self.character_service.get_all_characters(name, page)
            return jsonify({
                "data": data
            }), 200

        except Exception as e:
            print("ERRO NA CONTROLLER:", e)
            return jsonify({"error": "Server error"}), 500

    def get_character(self, id):
        try:
            data = self.character_service.get_character(id)

            return jsonify({"data": data}), 200
        
        except NotFound:
            return jsonify({"error": "Character not found"}), 404

        except Exception as e:
            print("ERRO NA CONTROLLER:", e)
            return jsonify({"error": "Server error"}), 500
        