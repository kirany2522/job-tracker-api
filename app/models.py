from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "company": self.company, "role": self.role}

