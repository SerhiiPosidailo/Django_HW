from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'updated_at', 'created_at', 'user')
        read_only_fields = ('id', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at',
        )
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data: dict):
        # Перевірте, чи 'name' присутній в validated_data перед вилученням його
        name = validated_data.get('name', None)
        surname = validated_data.pop('surname', None)
        age = validated_data.pop('age', None)

        user = UserModel.objects.create_user(**validated_data, name=name, surname=surname, age=age)
        return user


