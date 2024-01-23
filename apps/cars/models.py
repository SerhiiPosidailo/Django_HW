from django.db import models

from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    number_of_seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()

