from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    model = models.CharField(max_length=20, validators=[V.RegexValidator(Regex.MODEL.pattern, Regex.MODEL.msg)])
    year = models.IntegerField()
    number_of_seats = models.IntegerField(validators=[V.MinValueValidator(2), V.MaxValueValidator(8)])
    body_type = models.CharField(max_length=20)
    engine_capacity = models.FloatField()
    auto_parks = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()

