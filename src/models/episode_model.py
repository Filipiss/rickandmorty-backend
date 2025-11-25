from src.models import db, ma

class Episode(db.Model):
    __tablename__ = 'episodes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    air_date = db.Column(db.Date, nullable=False)
    episode = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Episode {self.name}>"
    
    print(episode)

class EpisodeOutput(ma.Schema):
    id = ma.Integer()
    name = ma.String()
    air_date = ma.Date()
    episode = ma.String()
