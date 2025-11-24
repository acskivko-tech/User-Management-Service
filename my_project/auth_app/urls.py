from django.urls import path

from auth_app.views import CreateUserAPIView

urlpatterns = [
    path('user/create',CreateUserAPIView.as_view(),name='create_user'),
]