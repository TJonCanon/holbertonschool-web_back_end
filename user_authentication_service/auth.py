#!/usr/bin/env python3
""" authentication service """


from bcrypt import hashpw, gensalt, checkpw
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """ salty hashbrowns """
    return hashpw(password.encode(), gensalt())

def _generate_uuid() -> str:
    """ creates new user_id """
    return str(uuid.uuid4())

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

    def valid_login(self, email: str, password: str) -> bool:
        """ checks if login attempt is valid """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
