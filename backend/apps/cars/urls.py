from django.urls import path

from .views import CarAddAvatarView, CarListCreateView, CarsRetriveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarsRetriveUpdateDestroyView.as_view(), name='cars_retrieve_update_destroy'),
    path('/<int:pk>/avatar', CarAddAvatarView.as_view(), name='cars_add_photo')
]