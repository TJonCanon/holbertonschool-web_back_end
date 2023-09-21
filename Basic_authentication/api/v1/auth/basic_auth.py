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


    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """ returns the decoded value of a Base64 string """
        if not base64_authorization_header \
                or type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(
                base64_authorization_header
            ).decode('utf-8')
        except Exception:
            return None


    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """  returns the user email and password from the Base64 value """
        if decoded_base64_authorization_header is None \
                or type(decoded_base64_authorization_header) != str \
                or not re.search(':', decoded_base64_authorization_header):
            return None, None
        return tuple(re.split(':', decoded_base64_authorization_header))
