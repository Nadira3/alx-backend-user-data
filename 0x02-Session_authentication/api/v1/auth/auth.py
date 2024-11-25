#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for the given path.
        Supports wildcard patterns ('*') at the end of excluded paths.
        """
        if path is None or excluded_paths is None or not isinstance(
                excluded_paths, list):
            return True

        # Normalize path by removing trailing slashes
        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                # Match prefix up to the wildcard
                if path.startswith(excluded_path[:-1]):
                    return False
            elif path == excluded_path.rstrip('/'):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve Authorization header."""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
