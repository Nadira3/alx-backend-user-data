#!/usr/bin/env python3
"""
Module for filtering sensitive data in log messages.

This module contains the filter_datum function, which obfuscates
the values of specified fields in a given log message.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): A list of field names to be obfuscated.
        redaction (str): The string to replace the sensitive field values with.
        message (str): The log message that contains the fields.
        separator (str): The separator character between fields in the message.

    Returns:
        str: The log message with sensitive field values replaced by the redaction string.
    """
    return re.sub(r'({})=[^{}]+'.format('|'.join(fields), separator), r'\1=' + redaction, message)
