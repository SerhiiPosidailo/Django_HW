from django.urls import path

from .views import AutoParkListCreateAPIView, AutoParkAddCarView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateAPIView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view(), name='auto_park_retrieve_update_destroy'),
    path('/<int:pk>/cars', AutoParkAddCarView.as_view(), name='auto_park_add_car'),
]
