#!/usr/bin/env python3
"""
Basic Auth module for the API
"""


import base64
from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Authentication Class."""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract Base64 part of Authorization header."""
        if not authorization_header or not\
                isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string into a UTF-8 string
        """
        if base64_authorization_header is None or not isinstance(
                base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user email and password from Base64 decoded value
        """
        if decoded_base64_authorization_header is None or not\
                isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns a User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({'email': user_email})
            if not user or not user[0].is_valid_password(user_pwd):
                return None
            return user[0]
        except Exception:
            return None
