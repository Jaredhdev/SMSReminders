from app import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Task {self.description}>'
