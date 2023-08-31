from functools import wraps
from flask import request
from firebase_admin import auth

from app import error_codes


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'X-Access-Tokens' in request.headers:
            token = request.headers['X-Access-Tokens']
        if not token:
            return error_codes.BAD_REQUEST, 400

        try:
            auth.verify_id_token(token)
        except auth.ExpiredIdTokenError:
            return error_codes.JWT_EXPIRED, 401
        except auth.InvalidIdTokenError:
            return error_codes.JWT_INVALID, 401
        except Exception:
            return error_codes.JWT_OTHER, 401

        return f(*args, **kwargs)

    return decorator
