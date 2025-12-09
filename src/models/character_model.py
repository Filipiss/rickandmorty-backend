from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property

class Character(db.Model):
    __tablename__ = 'characters'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=True)
    gender = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    
    origin_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=True)

    origin = db.relationship(
        "Location",
        foreign_keys=[origin_id],
        back_populates="origin_characters",
        uselist=False,
        lazy=True
    )

    location = db.relationship(
        "Location",
        foreign_keys=[location_id],
        back_populates="current_characters",
        uselist=False,
        lazy=True
    )

    episodes = db.relationship(
        "Episode",
        secondary="characters_episodes",
        back_populates="characters"
    )

    @hybrid_property
    def last_episode(self):
        if not self.episodes:
            return None
        
        return max(self.episodes, key=lambda ep: ep.id)

    def __repr__(self):
        return f"<Character {self.name}>"
    
class CharacterOutputGetAll(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    status = ma.String()
    species = ma.String()
    image = ma.String()


class CharacterOutputGetById(CharacterOutputGetAll):
    type = ma.String()
    gender = ma.String()
    last_episode = ma.Nested("EpisodeOutput")

    origin = ma.Nested(
        "LocationOutput",
        allow_none=True
    )

    location = ma.Nested(
        "LocationOutput",
        allow_none=True
    )

    episodes = ma.List(
        ma.Nested("EpisodeOutput")
    )

class CharacterMetaOutput(ma.Schema):
    current_page = ma.Integer()
    per_page = ma.Integer()
    total_results = ma.Integer()
    total_pages = ma.Integer()

character_output_get_all = CharacterOutputGetAll()
character_output_get_by_id = CharacterOutputGetById()
character_meta_output = CharacterMetaOutput()
