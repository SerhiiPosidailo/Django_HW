from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from drf_yasg.utils import swagger_auto_schema

from .filters import CarFilter
from .models import CarModel
from .serializers import CarAvatarSerializer, CarSerializer


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class CarListCreateView(ListCreateAPIView):
    """
        get:
            Returns all list
        post:
            Creates a new Car
    """
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarsRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarAddAvatarView(UpdateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = CarAvatarSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('put',)

    def perform_update(self, serializer):
        car: CarModel = self.get_object()
        car.avatar.delete()
        super().perform_update(serializer)
