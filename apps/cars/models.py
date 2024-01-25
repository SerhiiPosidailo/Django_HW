from django.db import models

from apps.auto_parks.models import AutoParkModel
from core.models import BaseModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    model = models.CharField(max_length=20)
    year = models.IntegerField()
    number_of_seats = models.IntegerField()
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

