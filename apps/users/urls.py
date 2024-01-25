from django.urls import path

from apps.users.views import UserListCreateView, UserAddAutoParkView, UserListAutoParkView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserAddAutoParkView.as_view(), name='create_user'),
    path('/<int:pk>/autoparks', UserListAutoParkView.as_view(), name='users')
]