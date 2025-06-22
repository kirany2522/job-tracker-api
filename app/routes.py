from app import app
from flask import jsonify

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Job Tracker API 🚀"})

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    # Sample static data (we’ll connect DB later)
    jobs = [
        {"id": 1, "company": "Google", "role": "Backend Developer"},
        {"id": 2, "company": "Amazon", "role": "Full Stack Developer"}
    ]
    return jsonify(jobs)
