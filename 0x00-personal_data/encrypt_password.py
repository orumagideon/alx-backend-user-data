#!/usr/bin/env python3
"""A module dedicated to password encryption."""
import bcrypt

def hash_password(password: str) -> bytes:
    """Generates a hashed password using a random salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Verifies if a given password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
