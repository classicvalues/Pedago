# pedago/api.py

from flask import Flask, request, jsonify
from pedago.course.course_manager_wrapper import CourseManagerWrapper

app = Flask(__name__)
course_manager = CourseManagerWrapper()

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    course_id = course_manager.createCourse(data['title'], data['description'], data['start_date'], data['end_date'], data['teacher_id'])
    return jsonify({'course_id': course_id})

@app.route('/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    course = course_manager.getCourse(course_id)
    return jsonify(course)

if __name__ == '__main__':
    app.run(debug=True)
