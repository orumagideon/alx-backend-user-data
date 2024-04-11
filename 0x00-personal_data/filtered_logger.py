#!/usr/bin/env python3
"""A module for log filtering."""
import os
import re
import logging
import mysql.connector
from typing import List

# Define patterns for extracting and replacing fields
patterns = {
    'extract': lambda fields, separator: r'(?P<field>{})=[^{}]*'.format('|'.join(fields), separator),
    'replace': lambda redaction: r'\g<field>={}'.format(redaction),
}

# Define fields considered as Personally Identifiable Information (PII)
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Filters sensitive information in a log line."""
    return re.sub(patterns"extract", patterns"replace", message)

def get_logger() -> logging.Logger:
    """Creates a logger for user data."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.addHandler(logging.StreamHandler().setFormatter(RedactingFormatter(PII_FIELDS)))
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """Establishes a connection to the database."""
    connection = mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        port=3306,
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME", ""),
    )
    return connection

def main():
    """Logs user records from a database table after filtering sensitive information."""
    fields = "name,email,phone,ssn,password,ip,last_login,user_agent"
    query = f"SELECT {fields} FROM users;"
    logger = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        for row in cursor.fetchall():
            record = map(lambda item: f'{item[0]}={item[1]}', zip(fields.split(','), row))
            log_record = logging.LogRecord("user_data", logging.INFO, None, None, '; '.join(record), None, None)
            logger.handle(log_record)

class RedactingFormatter(logging.Formatter):
    """A formatter that redacts sensitive information in logs."""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats a LogRecord, redacting sensitive information."""
        return filter_datum(self.fields, self.REDACTION, super().format(record), ';')

if __name__ == "__main__":
    main()

