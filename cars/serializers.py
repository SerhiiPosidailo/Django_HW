from rest_framework import serializers
from cars.models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=20)
    year = serializers.IntegerField()


class CarSerializerAll(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    model = serializers.CharField(max_length=20)
    year = serializers.IntegerField()
    number_of_seats = serializers.IntegerField()
    body_type = serializers.CharField(max_length=20)
    engine_capacity = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data:dict):
        for k, v in validated_data.items():
            setattr(instance, k, v)
        instance.save()
        return instance






