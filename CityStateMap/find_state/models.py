from django.db import models
from pydantic import BaseModel


class City(BaseModel):
    """
    Class represent the model for request data in fastapi to contain a json with city_name as key and value which is
    going to be provided by the user
    """
    city_name: str


class Location(BaseModel):
    """
    Class represents the modal for request data in fastapi to contain a json with latitude_longitude as key and its
    value which is provided by the user
    """
    latitude_longitude: str
