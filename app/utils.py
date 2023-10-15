"""
Utils submodule contains common helper functions
that can be utilized by other functions.
"""

from functools import wraps
from typing import Callable
from flask import request
from firebase_admin import auth

from app import error_codes


def token_required(func: Callable) -> Callable:
    """
    This is a wrapper function ensuring that the request
    passed to wrapped endpoint contains the 'X-Access-Tokens'
    header acquired by authentication endpoint.

    Args:
        func (Callable): Function (endpoint) to wrap.

    Returns:
        Callable: Wrapped function ensuring that the provided
                  token is valid and current.
    """
    @wraps(func)
    def decorator(*args: tuple, **kwargs: dict[str, any]) \
            -> tuple or None:
        """
        This function checks if provided request's headers
        contain 'X-Access-Tokens' (set by Auth endpoint) and
        verifies whether the token is valid and not expired.

        Args:
            args (tuple): Non-keyword arguments of wrapped function.
            kwargs (dict[str, any]): Keyword arguments of wrapped function.

        Returns:
            (tuple): (Error signature, status code) - if the token is
                    invalid, else None.
        """
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

        return func(*args, **kwargs)

    return decorator
