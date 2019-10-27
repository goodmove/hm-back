from flask import Flask, request

from src.main.api.common import error_response, success_response
from src.main.database.answers import (find_one_answer,
                                       find_all_answers,
                                       find_user_answers,
                                       find_meme_answers,
                                       insert_answer)
from src.main.database.users import find_one_user, update_user
from src.main.database.memes import find_one_meme, update_meme
from src.main.model.answer import Answer
from src.main.model.meme import Meme
from src.main.model.user import User


def init(app: Flask):
    @app.route('/api/answers/<string:answer_id>')
    def get_answer(answer_id):
        res = find_one_answer(answer_id)
        if res:
            result_json = Answer.from_bson(res).to_json()
            return success_response({'answer': result_json})
        else:
            return error_response('Answer with id {} not found'.format(answer_id), 404, None)

    @app.route('/api/answers', methods=['POST'])
    def post_answer():
        body = request.json
        meme_id = body['memeId']
        user_id = body['userId']
        result = body['result']
        feedback = body.get('feedback')
        # insert_answer(meme_id, user_id, subject_id, result, feedback)

        # Update Meme
        meme = Meme.from_bson(find_one_meme(meme_id))
        update_meme(meme_id, {'shown': meme.shown + 1})
        if result == 'correct':
            update_meme(meme_id, {'answered_correctly': meme.answered_correctly + 1})
        if result == 'incorrect':
            update_meme(meme_id, {'answered_incorrectly': meme.answered_incorrectly + 1})

        # Update urer
        user = User.from_bson(find_one_user(user_id))
        update_user(user_id, {'memes_shown': user.memes_shown + 1})
        if result == 'correct':
            update_user(user_id, {'correct_answers': user.correct_answers + 1})
        if result == 'incorrect':
            update_user(user_id, {'incorrect_answers': user.incorrect_answers + 1})

        return success_response({})

    @app.route('/api/answers/list_answers')
    def list_answers():
        answers = find_all_answers()
        return success_response({'answers': [m.to_json() for m in answers]})

    @app.route('/api/answers/list_meme_answers', methods=['POST'])
    def list_meme_answers():
        body = request.json
        meme_id = body['meme_id']
        answers = find_meme_answers(meme_id)
        return success_response({'answers': [m.to_json() for m in answers]})

    @app.route('/api/answers/list_user_answers', methods=['POST'])
    def list_user_answers():
        body = request.json
        user_id = body['user_id']
        answers = find_user_answers(user_id)
        return success_response({'user_answers': [m.to_json() for m in answers]})
