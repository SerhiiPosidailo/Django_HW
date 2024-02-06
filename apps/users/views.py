from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from core.dataclasses.user_dataclass import UserDataClass
from core.permissions.is_admin_or_write_only_permission import IsAdminOrWriteOnlyPermission
from core.permissions.permissions_admin_user import IsSuperUser

from apps.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminOrWriteOnlyPermission,)


class MeView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if user.is_staff:
            user.is_staff = False
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if not user.is_staff:
            user.is_staff = True
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UserBlockView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()


    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if user.is_active:
            user.is_active = False
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UserUnBlockView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def patch(self, *args, **kwargs):
        user: UserDataClass = self.get_object()
        if not user.is_active:
            user.is_active = True
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)
