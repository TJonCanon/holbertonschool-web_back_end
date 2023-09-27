#!/usr/bin/env python3
""" authentication with python3 """


from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class for authentication """
from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class for authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if authenticated, else False"""
        if not path or not excluded_paths:
            return True
        return False if os.path.join(path, '') in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ returns Flask request """
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns Flask request """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None
        return request.cookies.get(os.getenv('SESSION_NAME'))
