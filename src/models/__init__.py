from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
  

db = SQLAlchemy()
ma = Marshmallow()

from src.models.character_model import Character
from src.models.location_model import Location
from src.models.episode_model import Episode
from src.models.character_episode_model import CharacterEpisode 
