from django.urls import path

from .views import CarListCreateView, CarsRetriveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarsRetriveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy')
]