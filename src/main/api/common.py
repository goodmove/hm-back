from typing import Optional

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
