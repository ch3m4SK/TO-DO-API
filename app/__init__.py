from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    ma.init_app(app)
    
    # Registrar rutas
    from app.routes import register_routes
    register_routes(app)
    
    with app.app_context():
        db.create_all()
    
    return app