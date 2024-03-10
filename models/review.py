#!/usr/bin/python3
"""
module for Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    documentation for Review class that inherits
    from the BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
