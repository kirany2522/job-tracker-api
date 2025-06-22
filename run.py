from app import app

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
db = SQLAlchemy(app)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    new_job = Job(company=data['company'], role=data['role'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job added successfully!'})

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    output = []
    for job in jobs:
        output.append({
            'id': job.id,
            'company': job.company,
            'role': job.role
        })
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
