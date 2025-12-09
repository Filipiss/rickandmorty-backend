from src.models import db, ma
from sqlalchemy.ext.hybrid import hybrid_property

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    dimension = db.Column(db.String(50), nullable=False)

    origin_characters = db.relationship(
        "Character",
        foreign_keys="Character.origin_id",
        back_populates="origin",
        uselist=True,
        lazy=True
    )

    
    current_characters = db.relationship(
        "Character",
        foreign_keys="Character.location_id",
        back_populates="location",
        uselist=True,
        lazy=True
    )

    @hybrid_property
    def current_residents_count(self):
        return len(self.current_characters)
   
class LocationOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    type = ma.String()
    dimension = ma.String()
    current_residents_count = ma.Integer()

    
