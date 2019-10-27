from flask import Flask, request

from src.main.api.common import error_response, success_response
from src.main.database.subjects import find_one_subject, find_all_subjects, insert_subject
from src.main.model.subject import Subject


def init(app: Flask):
    @app.route('/api/subjects/<string:subject_id>')
    def get_subject(subject_id):
        res = find_one_subject(subject_id)
        if res:
            subject_json = Subject.from_bson(res).to_json()
            return success_response({'subject': subject_json})
        else:
            return error_response('Subject with id {} not found'.format(subject_id), 404, None)

    @app.route('/api/subjects/')
    def list_subjects():
        subjects = find_all_subjects()
        return success_response({'subjects': subjects})

    @app.route('/api/subjects/', methods=['POST'])
    def add_subject():
        body = request.json
        subject = insert_subject(body['name'])
        return success_response({'subject': subject.to_json()})
