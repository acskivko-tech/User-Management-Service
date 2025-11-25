from django.urls import path

from auth_app.views import CreateUserAPIView, UserAPIListView, IDUserAPIUpdateView, CurrentUserUpdateAPIView

urlpatterns = [
    path('user/create',CreateUserAPIView.as_view(),name='create_user'),
    path('user/update/<int:pk>',IDUserAPIUpdateView.as_view(),name='id_user_update'),
    path('user/update/current',CurrentUserUpdateAPIView.as_view(),name='current_user_update'),
    path('users/list',UserAPIListView.as_view(),name='user_list'),
]