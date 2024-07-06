#models.py
from app import db

class Vacancy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    salary_from = db.Column(db.Integer)
    salary_to = db.Column(db.Integer)
    employment_format = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment_format': self.employment_format,
            'created_at': self.created_at.isoformat()
        }

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.Text)
    employment_format = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'position': self.position,
            'skills': self.skills,
            'employment_format': self.employment_format,
            'created_at': self.created_at.isoformat()
        }
