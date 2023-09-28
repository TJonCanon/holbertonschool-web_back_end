#!/usr/bin/env python3
"""
authentication service
"""


from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ salty hashbrowns """
    return hashpw(password.encode(), gensalt())
