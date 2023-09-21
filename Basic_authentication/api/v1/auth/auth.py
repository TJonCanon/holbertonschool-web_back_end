#!/usr/bin/env python3
"""
authentication with python3
"""


from flask import request
from typing import List, TypeVar

class Auth():
    """ Auth class for authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if authenticated, else False"""
        return False

    def authorization_header(self, request=None) -> str:
        """ returns Flask request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns Flask request """
        return None
