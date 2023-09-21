#!/usr/bin/env python3
""" authentication with python3 """


from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ Auth class for authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ returns True if authenticated, else False"""
        if not path or not path or excluded_paths:
            return True
        return False if os.path.join(path,
        '') in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ returns Flask request """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns Flask request """
        return None
