from typing import Optional

from flask import Flask
from flask.json import jsonify


def error_response(message: str, code: int, payload: Optional[dict]):
    if not payload:
        payload = dict()
    result = {
        'result': 'error',
        'payload': payload,
        'code': code,
        'message': message,
    }
    return jsonify(result), code


def success_response(payload: dict, code: Optional[int] = None):
    if not code:
        code = 200
    result = {
        'result': 'success',
        'payload': payload
    }
    return jsonify(result), code


def init(app: Flask):
    @app.errorhandler(500)
    def server_error_wrapper(e: Exception):
        return error_response('Server Error', 500, {
            'message': str(e)
        })

    @app.after_request
    def inject_cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Method'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'

        return response
