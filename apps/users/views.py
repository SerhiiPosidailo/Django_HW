from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, get_object_or_404
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.users.models import UserModel
from apps.users.serializers import UserSerializer


class UserListCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserAddAutoParkView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, id=pk)
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        ap_serializer = UserSerializer(user)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)


class UserListAutoParkView(ListAPIView):
    serializer_class = AutoParkSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return AutoParkModel.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        for autopark_data in data:
            autopark_id = autopark_data['id']
            cars_without_user = AutoParkModel.objects.get(id=autopark_id).cars.filter(auto_parks_id__isnull=True)
            autopark_data['cars'] = AutoParkSerializer(cars_without_user, many=True).data

        return Response(data)










