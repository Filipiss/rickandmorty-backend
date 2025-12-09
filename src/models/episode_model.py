from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.Date, nullable=False)
    episode = db.Column(db.String(50), nullable=False)

    characters = db.relationship(
        "Character",
        secondary="characters_episodes",
        back_populates="episodes"
    )
    def __repr__(self):
        return f"<Episode {self.name}>"
    

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.Date()
    episode = ma.String()