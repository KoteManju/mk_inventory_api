# run.py

from app import create_app, db

# Create the Flask application
app = create_app()  # or create_app() for default config

if __name__ == "__main__":
    with app.app_context():
        # Create all database tables
        db.create_all()
        print("✅ Database tables created successfully!")
    
    print("🚀 Starting Flask application...")
    print("📖 Swagger documentation available at: http://localhost:5000/apidocs/")
    print("🔍 API specification available at: http://localhost:5000/apispec.json")
    
    app.run(debug=True, host='0.0.0.0', port=5000)