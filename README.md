# Inventory API

A simple REST API built with Flask, SQLAlchemy, Marshmallow, and JWT.

## Auth Endpoints
- POST /auth/register
- POST /auth/login

## Protected Item Routes
- GET /items/
- POST /items/

Include Authorization header: Bearer <token>

## Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
python run.py
```

## Run Tests
```
pytest tests/
```