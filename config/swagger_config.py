# config/swagger_config.py

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Inventory API",
        "description": "API for managing inventory items with JWT authentication",
        "version": "1.0.0",
        "contact": {
            "name": "API Support",
            "email": "support@example.com"
        }
    },
    "host": "localhost:5000",
    "basePath": "/api",
    "schemes": ["http", "https"],
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
        }
    },
    "definitions": {
        "Item": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "Unique identifier for the item",
                    "example": 1
                },
                "name": {
                    "type": "string",
                    "description": "Name of the item",
                    "example": "Sample Item"
                },
                "description": {
                    "type": "string",
                    "description": "Description of the item",
                    "example": "This is a sample item description"
                },
                "price": {
                    "type": "number",
                    "format": "float",
                    "description": "Price of the item",
                    "example": 29.99
                },
                "category": {
                    "type": "string",
                    "description": "Category of the item",
                    "example": "Electronics"
                },
                "quantity": {
                    "type": "integer",
                    "description": "Available quantity",
                    "example": 10
                },
                "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Creation timestamp"
                },
                "updated_at": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Last update timestamp"
                }
            },
            "required": ["id", "name"]
        },
        "ItemInput": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Name of the item",
                    "example": "Sample Item"
                },
                "description": {
                    "type": "string",
                    "description": "Description of the item",
                    "example": "This is a sample item description"
                },
                "price": {
                    "type": "number",
                    "format": "float",
                    "description": "Price of the item",
                    "example": 29.99
                },
                "category": {
                    "type": "string",
                    "description": "Category of the item",
                    "example": "Electronics"
                },
                "quantity": {
                    "type": "integer",
                    "description": "Available quantity",
                    "example": 10
                }
            },
            "required": ["name"]
        },
        "ErrorResponse": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "Error message"
                },
                "errors": {
                    "type": "object",
                    "description": "Detailed error information"
                }
            }
        }
    }
}