from django.urls import path

from .views import UsersAddAutoParkView, UsersListCreateView, UsersRetrieveUpdateDestroyView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/<int:pk>', UsersRetrieveUpdateDestroyView.as_view(), name='users_retrieve_update_destroy'),
    path('/<int:pk>/auto_parks', UsersAddAutoParkView.as_view(), name='users_add_auto_park')
]