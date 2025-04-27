from main import app, db
from models import Correction

with app.app_context():
    db.drop_all()  # Drop all tables
    db.create_all()  # Create all tables
    # Add initial data if needed
    sample = Correction(text="Sample text", 
                        correction="Sample correction",
                        is_misinformation=False)
    db.session.add(sample)
    db.session.commit()  # Commit the changes to the database

    print("Database initialized and sample data added successfully in poc_corrections.db")