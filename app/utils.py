from functools import wraps
from flask import request
from firebase_admin import auth


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'X-Access-Tokens' in request.headers:
            token = request.headers['X-Access-Tokens']

        if not token:
            return "No JWT token provided.", 400
        try:
            auth.verify_id_token(token)
        except Exception as e:
            print(e)
            return "Invalid JWT token.", 400

        return f(*args, **kwargs)

    return decorator
