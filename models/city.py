#!/usr/bin/python3
"""
    City Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class that inherits from BaseModel"""
    name = ""
    state_id = ""
