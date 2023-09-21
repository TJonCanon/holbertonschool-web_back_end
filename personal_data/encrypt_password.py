#!/usr/bin/env python3
""" encryption module """

import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password as a byte string """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
