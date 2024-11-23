#!/usr/bin/env python3


"""
Module for filtering sensitive data in log messages.

This module contains the filter_datum function, which obfuscates
the values of specified fields in a given log message.
"""


import logging
import re
from typing import List


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
    return re.sub(r'(' + '|'.join([re.escape(field) for field in fields]) + r')=[^' + re.escape(separator) + r']+', 
                  lambda m: m.group(0).split('=')[0] + '=' + redaction, message).replace(";", "; ")


class RedactingFormatter(logging.Formatter):
    """
        Redacting Formatter class that filters
        sensitive data from log messages.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter with the fields to filter.

        Args:
            fields (List[str]): A list of field names to be obfuscated
            in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, replacing specified fields
        with redaction string.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with filtered field values.
        """
        return super(RedactingFormatter, self).format(record).replace(record.msg, filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR))
