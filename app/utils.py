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
            return "No JWT token provided.", 401

        try:
            auth.verify_id_token(token)
        except auth.ExpiredIdTokenError:
            return "JWT token has expired.", 402
        except auth.InvalidIdTokenError:
            return "Invalid JWT token.", 401

        return f(*args, **kwargs)

    return decorator