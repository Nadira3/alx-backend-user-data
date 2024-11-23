#!/usr/bin/env python3


"""
Module for filtering sensitive data in log messages.

This module contains the filter_datum function, which obfuscates
the values of specified fields in a given log message.
"""

import logging
import re
from typing import List, Tuple
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.
    Args:
        fields (List[str]): A list of field names to be obfuscated.
        redaction (str): The string to replace the sensitive field values with.
        message (str): The log message that contains the fields.
        separator (str): The separator character between fields in the message.

    Returns:
        str: The log message with sensitive field values replaced
        by the redaction string.
    """
    obfuscated_message = re.sub(
        r'(' + '|'.join([re.escape(field) for field in fields
                         ]) + r')=[^' + re.escape(separator) + r']+',
        lambda m: m.group(0).split('=')[0] + '=' + redaction,
        message
    )
    parts = obfuscated_message.split(separator)
    return f"{separator} ".join(parts[:-1]) + separator + parts[-1]


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log message, obfuscating sensitive fields.
        """
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named "user_data".
    The logger will only log up to INFO level, and it will not propagate
    messages to other loggers. It includes a StreamHandler with
    a RedactingFormatter to filter sensitive information.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Returns a connector to the database.

    Uses environment variables for database credentials:
        - PERSONAL_DATA_DB_USERNAME (default: "root")
        - PERSONAL_DATA_DB_PASSWORD (default: "")
        - PERSONAL_DATA_DB_HOST (default: "localhost")
        - PERSONAL_DATA_DB_NAME (no default, required)

    Returns:
        MySQLConnection: A connection to the database.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    if not database:
        raise ValueError("Environment variable\
                         PERSONAL_DATA_DB_NAME must be set.")

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
