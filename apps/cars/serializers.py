from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'number_of_seats', 'body_type', 'engine_capacity', 'created_at', 'updated_at')

    def validate_model(self, value):
        if value == 'lada':
            raise ValidationError({'details': 'model == lada'})
        return value

    def validate(self, item):
        if item['number_of_seats'] == item['engine_capacity']:
            raise ValidationError({'details': 'number_of_seats == engine_capacity'})
        return item


            