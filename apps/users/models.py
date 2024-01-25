from django.db import models

from core.models import BaseModel


class UserModel(BaseModel):
    class Meta:
        db_table = 'user'

    name = models.CharField(max_length=10)

