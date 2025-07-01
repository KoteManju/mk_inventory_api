from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    from .routes.item_routes import item_bp
    from .routes.auth_routes import auth_bp
    app.register_blueprint(item_bp, url_prefix='/items')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app






# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_jwt_extended import JWTManager
# from .config import Config
# from flasgger import Swagger

# db = SQLAlchemy()
# ma = Marshmallow()
# jwt = JWTManager()
# swagger = Swagger()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
#     app.config['JWT_IDENTITY_CLAIM'] = 'sub'

#     db.init_app(app)
#     ma.init_app(app)
#     jwt.init_app(app)
#     swagger.init_app(app)

#     # Register blueprints
#     from .routes.item_routes import item_bp
#     from .routes.auth_routes import auth_bp

#     app.register_blueprint(item_bp, url_prefix='/items')
#     app.register_blueprint(auth_bp, url_prefix='/auth')

#     # with app.app_context():
#     #     db.create_all()

#     return app




# app/__init__.py

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flasgger import Swagger
# from config.swagger_config import SWAGGER_CONFIG, SWAGGER_TEMPLATE

# # Initialize extensions
# db = SQLAlchemy()
# migrate = Migrate()

# def create_app(config_name='default'):
#     app = Flask(__name__)
    
#     # Load configuration
#     if config_name == 'development':
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         app.config['SECRET_KEY'] = 'your-secret-key-here'
#         app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
#     else:
#         # Default configuration
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#         app.config['SECRET_KEY'] = 'your-secret-key-here'
#         app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'
    
#     # Initialize extensions with app
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     # Initialize Swagger
#     swagger = Swagger(app, config=SWAGGER_CONFIG, template=SWAGGER_TEMPLATE)
    
#     # Import and register blueprints (after db initialization to avoid circular imports)
#     with app.app_context():
#         # Import models here to ensure they are registered with SQLAlchemy
#         from app.models.item import Item
#         from app.models.user import User  # Assuming you have a User model
        
#         # Register blueprints
#         from app.routes.item_routes import item_bp
#         from app.routes.auth_routes import auth_bp  # Assuming you have auth routes
        
#         app.register_blueprint(item_bp, url_prefix='/api/items')
#         app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
#     return app


# ==========

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_jwt_extended import JWTManager
# from flasgger import Swagger
# from .config import Config

# db = SQLAlchemy()
# ma = Marshmallow()
# jwt = JWTManager()

# swagger_config = {
#     "headers": [],
#     "specs": [
#         {
#             "endpoint": 'apispec_1',
#             "route": '/apispec_1.json',
#             "rule_filter": lambda rule: True,
#             "model_filter": lambda tag: True,
#         }
#     ],
#     "static_url_path": "/flasgger_static",
#     "swagger_ui": True,
#     "specs_route": "/apidocs/"
# }

# swagger_template = {
#     "swagger": "2.0",
#     "info": {
#         "title": "Inventory API",
#         "description": "API documentation for managing inventory items and user authentication",
#         "version": "1.0.0"
#     },
#     "securityDefinitions": {
#         "Bearer": {
#             "type": "apiKey",
#             "name": "Authorization",
#             "in": "header",
#             "description": "JWT Authorization header using the Bearer scheme. Example: 'Authorization: Bearer {token}'"
#         }
#     },
#     "security": [{"Bearer": []}]
# }

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     ma.init_app(app)
#     jwt.init_app(app)

#     Swagger(app, config=swagger_config, template=swagger_template)

#     from .routes.item_routes import item_bp
#     from .routes.auth_routes import auth_bp
#     app.register_blueprint(item_bp, url_prefix='/items')
#     app.register_blueprint(auth_bp, url_prefix='/auth')

#     return app

