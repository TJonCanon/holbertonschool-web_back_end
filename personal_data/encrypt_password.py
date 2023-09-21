#!/usr/bin/env python3
""" encryption module """

import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password as a byte string """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ checks a hashed_password against the real deal """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
