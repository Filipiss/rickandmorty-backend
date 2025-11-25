from src.models import db, ma
from marshmallow import fields

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

    origin = db.relationship(
        "Location",
        foreign_keys=[origin_id],
        back_populates="origin_characters"
    )

    location = db.relationship(
        "Location",
        foreign_keys=[location_id],
        back_populates="current_characters"
    )

    episodes = db.relationship(
        "Episode",
        secondary="characters_episodes",
        back_populates="characters"
    )


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

    origin = fields.Nested(
        "LocationOutput",
        only=("id", "name"),
        allow_none=True
    )

    location = fields.Nested(
        "LocationOutput",
        only=("id", "name"),
        allow_none=True
    )

    episodes = fields.List(
        fields.Nested("EpisodeOutput", only=("id", "name"))
    )


character_output = CharacterOutput()
characters_output = CharacterOutput(many=True)
