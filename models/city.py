#!/usr/bin/python3
"""module for city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class for handling city data"""
    state_id = ""
    name = ""
