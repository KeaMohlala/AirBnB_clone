#!/usr/bin/python3
"""
module the for User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    defines the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
