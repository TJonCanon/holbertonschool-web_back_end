#!/usr/bin/env python3
""" basic authentication mechanism """


from api.v1.auth.auth import Auth
import re
import base64


class BasicAuth(Auth):
    """ basic auth class inheriting from Auth """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if not authorization_header \
                or type(authorization_header) is not str \
                or not re.search("^Basic ", authorization_header):
            return None
        return re.sub("^Basic ", "", authorization_header)
