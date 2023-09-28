#!/usr/bin/env python3
"""
authentication service
"""


from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ salty hashbrowns """
    return hashpw(password.encode(), gensalt())

class Auth:
    """ authentication class """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ registers a new user """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
