from flask import Flask, request

from src.main.api.amazon import upload_file
from src.main.api.common import error_response, success_response
from src.main.database.memes import find_one_meme, find_subject_memes, find_all_memes, insert_meme
from src.main.database.users import find_one_user
from src.main.model.meme import Meme
from src.main.api.quotes import *

import uuid

def get_next_meme_id(user_id, subject_id):
    user = find_one_user(user_id)
    if user.memes_shown > 0:
        user_strength = user.correct_answers / user.memes_shown
    else:
        user_strength = 0

    memes = find_subject_memes(subject_id)
    differences = []
    for meme in memes:
        if meme.shown > 0:
            meme_difficulty = meme.answered_correctly / meme.shown
        else:
            meme_difficulty = 0
        differences.append(abs(meme_difficulty - user_strength))
    min_index = differences.index(min(differences))
    return memes[min_index].id


def init(app: Flask):

    @app.route('/api/memes/<string:meme_id>')
    def get_meme(meme_id):
        res = find_one_meme(meme_id)
        if res:
            result_json = Meme.from_bson(res).to_json()
            return success_response({'meme': result_json})
        else:
            return error_response('Meme with id {} not found'.format(meme_id), 404, None)

    @app.route('/api/memes/next', methods=['POST'])
    def get_next_meme():
        body = request.json
        user_id = body['user_id']
        subject_id = body['subject_id']
        meme_id = get_next_meme_id(user_id, subject_id)
        meme = find_one_meme(meme_id)
        return success_response({'meme_id': meme.id,
                                'url': meme.url,
                                'explanation': meme.explanation,
                                'shown': meme.shown,
                                'answered_correctly': meme.answered_correctly,
                                'answered_incorrectly': meme.answered_incorrectly})

    @app.route('/api/memes/')
    def list_memes():
        memes = find_all_memes()
        return success_response({'memes': [m.to_json() for m in memes]})

    @app.route('/api/memes/', methods=['POST'])
    def add_meme():
        body = request.json
        meme = insert_meme(body['url'],
                            body['subject_id'],
                            body['explanation'],
                            0,
                            0,
                            0
                )
        print(meme.to_json())
        return success_response({'meme': meme.to_json()})

    @app.route('/api/memes/generate', methods=['POST'])
    def generate_meme():
        subjectId = request.json['subjectId']
        file_path = get_quoted_meme(request.json['caption'])
        description = get_quote(request.json['caption']) + 'said ' + request.json['caption']

        if file_path is None:
            return error_response('Failed to create mem', 500, {})

        image_key = str(uuid.uuid4()) + '.png'
        upload_file(file_path, image_key)
        meme = insert_meme(image_key, subjectId, description)
        image_url = 'https://hack-moscow-bucket.s3.eu-north-1.amazonaws.com/' + image_key
        return success_response({'image': {'id': meme.id, 'url': image_url}})

    @app.route('/api/memes/validate', methods=['POST'])
    def validate_meme():
        body = request.json
        imageId = body['id']
        decision = body['decision']
        print("Image decision:", imageId, decision)
        return success_response({})
