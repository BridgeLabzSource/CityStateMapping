from django.db import models
from pydantic import BaseModel


class City(BaseModel):
    city_name: str
