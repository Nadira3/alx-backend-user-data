#!/usr/bin/env python3
""" SessionAuth module """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class that manages session authentication"""
    # Class attribute for storing session data
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a given user_id.

        Args:
            user_id (str): The user's unique identifier.

        Returns:
            str: The created Session ID, or None if user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique Session ID
        session_id = str(uuid.uuid4())

        # Store the session_id-user_id pair in the dictionary
        self.user_id_by_session_id[session_id] = user_id

        return session_id
