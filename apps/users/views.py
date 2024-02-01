from rest_framework.generics import ListCreateAPIView

from apps.users.serializers import UserSerializer


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer


