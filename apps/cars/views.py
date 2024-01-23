from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .models import CarModel
from .serializers import CarSerializer
from .filters import cars_filter


class CarListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filter(self.request.query_params)


class CarsRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
