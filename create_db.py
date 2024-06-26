# create_db.py
from app import app, db

print("Attempting to create the database...")
with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
