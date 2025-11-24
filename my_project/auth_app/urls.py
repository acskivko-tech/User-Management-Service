from django.urls import path

from auth_app.views import CreateUserAPIView, UserAPIListView

urlpatterns = [
    path('user/create',CreateUserAPIView.as_view(),name='create_user'),
    path('users/list',UserAPIListView.as_view(),name='user_list'),
]