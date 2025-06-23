from app import app, db
from app.models import Job
from flask import request, jsonify, render_template

# ✅ Serve the dashboard frontend at root route
@app.route('/')
def home():
    return render_template('index.html')

# ✅ API to get all jobs
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])

# ✅ API to add a new job
@app.route('/api/jobs', methods=['POST'])
def add_job():
    data = request.get_json()

    # 🔒 Basic validation (optional, but good practice)
    if not data or 'company' not in data or 'role' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    new_job = Job(company=data['company'], role=data['role'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({"message": "Job added successfully!"}), 201
