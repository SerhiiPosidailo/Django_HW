from django.core import validators as V
from django.db import models

from core.enums.regex_enum import Regex
from core.models import BaseModel
from core.services.upload_avatar import upload_avatar

from apps.auto_parks.models import AutoParkModel
from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.managers import CarManager


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    model = models.CharField(max_length=20, validators=[V.RegexValidator(Regex.MODEL.pattern, Regex.MODEL.msg)])
    year = models.IntegerField()
    number_of_seats = models.IntegerField(validators=[V.MinValueValidator(2), V.MaxValueValidator(8)])
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    engine_capacity = models.FloatField()
    avatar = models.ImageField(blank=True, upload_to=upload_avatar)

    objects = CarManager()

