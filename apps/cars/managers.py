from django.db import models


class CarManager(models.Manager):
    def get_only_opel(self):
        return self.filter(model='opel')
