from app import app, db
from app.models import Job
from flask import request, jsonify

@app.route('/')
def home():
    return jsonify({"message": "Job Tracker API is Live!"})

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    new_job = Job(company=data['company'], role=data['role'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job added successfully!"}), 201
