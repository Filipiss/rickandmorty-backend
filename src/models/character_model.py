from src.models import db, ma
from marshmallow import validate

class Character(db.Model):
    __tablename__ = 'characters'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    
    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))


    def __repr__(self):
        return f"<Character {self.name}>"
    
class CharacterOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    type = ma.String()
    gender = ma.String()
    image = ma.String()
    origin_id = ma.Integer()
    location_id = ma.Integer()

character_output = CharacterOutput()
