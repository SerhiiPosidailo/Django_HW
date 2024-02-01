from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticated(),)
        return (AllowAny(),)

    def get_queryset(self):
        return UserModel.objects.exclude(pk=self.request.user.pk)

