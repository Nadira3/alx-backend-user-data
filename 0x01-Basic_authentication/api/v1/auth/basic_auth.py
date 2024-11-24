#!/usr/bin/env python3
"""
Basic Auth module for the API
"""


import base64
from api.v1.auth.auth import Auth


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
