from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    model = models.CharField(max_length=20, validators=[V.MinLengthValidator(3)])
    year = models.IntegerField()
    number_of_seats = models.IntegerField(validators=[V.MinValueValidator(2), V.MaxValueValidator(8)])
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

