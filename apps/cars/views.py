from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser

from .filters import CarFilter
from .models import CarModel
from .serializers import CarAvatarSerializer, CarSerializer


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


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
