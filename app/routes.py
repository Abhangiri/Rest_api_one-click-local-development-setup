from flask import Blueprint, request, jsonify
from app.models import db, Student
from flasgger import swag_from, Swagger

routes = Blueprint("routes", __name__)

@routes.route('/api/v1/students', methods=['POST'])
@swag_from({
    'tags': ['Students'],
    'summary': 'Create a new student',
    'description': 'Add a new student to the database',
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'required': True,
        'schema': {
            'id': 'Student',
            'required': ['name', 'age', 'grade'],
            'properties': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the student',
                    'example': 'John Doe'
                },
                'age': {
                    'type': 'integer',
                    'description': 'Age of the student',
                    'example': 20
                },
                'grade': {
                    'type': 'string',
                    'description': 'Grade of the student',
                    'example': 'A'
                }
            }
        }
    }],
    'responses': {
        201: {
            'description': 'Student created successfully',
            'schema': {
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Student added successfully'
                    }
                }
            }
        }
    }
})
def add_student():
    data = request.get_json()
    student = Student(name=data['name'], age=data['age'], grade=data['grade'])
    db.session.add(student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

@routes.route('/api/v1/students', methods=['GET'])
@swag_from({
    'tags': ['Students'],
    'summary': 'Get all students',
    'description': 'Returns a list of all students',
    'responses': {
        200: {
            'description': 'List of students',
            'schema': {
                'type': 'array',
                'items': {
                    'properties': {
                        'id': {
                            'type': 'integer',
                            'example': 1
                        },
                        'name': {
                            'type': 'string',
                            'example': 'John Doe'
                        },
                        'age': {
                            'type': 'integer',
                            'example': 20
                        },
                        'grade': {
                            'type': 'string',
                            'example': 'A'
                        }
                    }
                }
            }
        }
    }
})
def get_all_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "age": s.age, "grade": s.grade} for s in students])

@routes.route('/api/v1/students/<int:id>', methods=['GET'])
@swag_from({
    'tags': ['Students'],
    'summary': 'Get a specific student',
    'description': 'Returns a single student by ID',
    'parameters': [{
        'name': 'id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': 'ID of the student'
    }],
    'responses': {
        200: {
            'description': 'Student found',
            'schema': {
                'properties': {
                    'id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'name': {
                        'type': 'string',
                        'example': 'John Doe'
                    },
                    'age': {
                        'type': 'integer',
                        'example': 20
                    },
                    'grade': {
                        'type': 'string',
                        'example': 'A'
                    }
                }
            }
        },
        404: {
            'description': 'Student not found'
        }
    }
})
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({"id": student.id, "name": student.name, "age": student.age, "grade": student.grade})

@routes.route('/api/v1/students/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Students'],
    'summary': 'Update a student',
    'description': 'Update an existing student by ID',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the student'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'Student',
                'required': ['name', 'age', 'grade'],
                'properties': {
                    'name': {
                        'type': 'string',
                        'example': 'John Doe'
                    },
                    'age': {
                        'type': 'integer',
                        'example': 20
                    },
                    'grade': {
                        'type': 'string',
                        'example': 'A'
                    }
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Student updated successfully',
            'schema': {
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Student updated successfully'
                    }
                }
            }
        },
        404: {
            'description': 'Student not found'
        }
    }
})
def update_student(id):
    data = request.get_json()
    student = Student.query.get_or_404(id)
    student.name = data['name']
    student.age = data['age']
    student.grade = data['grade']
    db.session.commit()
    return jsonify({"message": "Student updated successfully"})

@routes.route('/api/v1/students/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Students'],
    'summary': 'Delete a student',
    'description': 'Delete a student by ID',
    'parameters': [{
        'name': 'id',
        'in': 'path',
        'type': 'integer',
        'required': True,
        'description': 'ID of the student to delete'
    }],
    'responses': {
        200: {
            'description': 'Student deleted successfully',
            'schema': {
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Student deleted successfully'
                    }
                }
            }
        },
        404: {
            'description': 'Student not found'
        }
    }
})
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})

@routes.route('/api/v1/healthcheck', methods=['GET'])
@swag_from({
    'tags': ['Health'],
    'summary': 'API Health Check',
    'description': 'Check if the API is running',
    'responses': {
        200: {
            'description': 'API is healthy',
            'schema': {
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'healthy'
                    }
                }
            }
        }
    }
})
def healthcheck():
    return jsonify({"status": "healthy"}), 200