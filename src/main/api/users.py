from flask import Flask, request

from src.main.api.common import error_response, success_response
from src.main.database.users import find_one_user, find_all_users, insert_user, update_user
from src.main.model.user import User


def init(app: Flask):
    @app.route('/api/users/<string:user_id>')
    def get_user(user_id):
        res = find_one_user(user_id)
        if res:
            result_json = User.from_bson(res).to_json()
            return success_response({'user': result_json})
        else:
            return error_response('User with id {} not found'.format(user_id), 404, None)

    @app.route('/api/users/')
    def list_users():
        data = find_all_users()
        return success_response({'users': [d.to_json() for d in data]})

    @app.route('/api/users/', methods=['POST'])
    def add_user():
        body = request.json
        inserted = insert_user(
            first_name=body['first_name'],
            last_name=body['last_name'],
            location=body.get('location'),
            age=body.get('age'),
            school=body.get('school'),
            interests=body.get('interests', []),
            memes_shown=0,
            correct_answers=0,
            incorrect_answers=0

        )
        return success_response({'user': inserted.to_json()})

    @app.route('/api/users/<user_id>', methods=['PUT'])
    def patch_user(user_id):
        body = request.json
        patch_object = {
            'first_name': body.get('first_name'),
            'last_name': body.get('last_name'),
            'location': body.get('location'),
            'age': body.get('age'),
            'school': body.get('school'),
            'interests': body.get('interests'),
            'memes_shown': body.get('memes_shown'),
            'correct_answers': body.get('correct_answers'),
            'incorrect_answers': body.get('incorrect_answers')
        }

        null_keys = []

        for key in patch_object:
            if not patch_object[key]:
                null_keys.append(key)

        for key in null_keys:
            del patch_object[key]

        return success_response(update_user(user_id, patch_object).to_json())
