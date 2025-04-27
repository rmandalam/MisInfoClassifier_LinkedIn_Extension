from main import db
from datetime import datetime, timezone

class Correction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    is_misinformation = db.Column(db.Boolean, default=False)
    correction = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)

    def __repr__(self):
        return f'<Correction {self.id}: {self.text} -> {self.correction}>'