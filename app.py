from flask import Flask
from src.models import db, ma
from config.settings import DATABASE_URI
from src.routes.character_routes import character_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(character_bp, url_prefix='/character')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
