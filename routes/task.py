from flask import Blueprint, request, jsonify
from models.task import Task
from flask_jwt_extended import jwt_required, get_jwt_identity

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.objects().to_json()
    return tasks

@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.json
    task = Task(title=data['title'], description=data['description'], user=get_jwt_identity())
    task.save()
    return jsonify({"message": "Task created successfully"})
