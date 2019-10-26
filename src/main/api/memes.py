from flask import Flask, request

from src.main.api.common import error_response, success_response
from src.main.database.memes import find_one_meme, get_all_memes, insert_meme
from src.main.model.meme import Meme


def init(app: Flask):
    @app.route('/api/memes/<string:meme_id>')
    def get_meme(meme_id):
        res = find_one_meme(meme_id)
        if res:
            result_json = Meme.from_bson(res).to_json()
            return success_response({'meme': result_json})
        else:
            return error_response('Meme with id {} not found'.format(meme_id), 404, None)

    @app.route('/api/memes/')
    def list_memes():
        memes = get_all_memes()
        return success_response({'memes': [m.to_json() for m in memes]})

    @app.route('/api/memes/', methods=['POST'])
    def add_meme():
        body = request.json
        meme = insert_meme(body['background_id'], body['text'], body['subject_id'])
        return success_response({'meme': meme.to_json()})
