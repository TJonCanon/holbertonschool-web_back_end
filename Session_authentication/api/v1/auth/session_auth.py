#!/usr/bin/env python3
""" session authentication """


from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """ new session authentication class inheriting from Auth """
    user_id_by_session_id = {}

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value """
        sesh = self.session_cookie(request)
        if sesh:
            user_id = self.user_id_for_session_id(sesh)
            if user_id:
                return User.get(user_id)
        return None

    def create_session(self, user_id: str = None) -> str:
        """ creates a session_id for a user """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a user_id based on a session_id """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
