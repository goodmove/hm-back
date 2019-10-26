from typing import Optional

from flask import Flask
from flask.json import jsonify

from src.main.database import find_one_subject

app = Flask(__name__)


@app.route('/')
def index():
    return "Home page content"


@app.route('/api/subjects/<int:subject_id>')
def get_subject(subject_id: int):
    subject_json = find_one_subject(subject_id)
    if subject_json:
        return jsonify(subject_json)
    else:
        return error_json('Subject with id {} not found'.format(subject_id), 404, None)


def error_json(message: str, code: int, payload: Optional[dict]):
    if not payload:
        payload = dict()
    result = {
        'result': 'error',
        'payload': payload,
        'code': code,
        'message': message,
    }
    return jsonify(result), code


app.run(host='0.0.0.0', port=5000)
