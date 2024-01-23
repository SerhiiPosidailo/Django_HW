from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'model', 'year', 'number_of_seats', 'body_type', 'engine_capacity', 'created_at', 'updated_at')

            