import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')

#DATABASE_URI = postgresql://postgres:123456@localhost:5432/rickandmorty