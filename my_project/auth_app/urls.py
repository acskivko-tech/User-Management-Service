from django.urls import path

from auth_app.views import CreateUserAPIView, UserAPIListView, IDUserAPIUpdateView, CurrentUserUpdateAPIView, \
    GetIDUserAPIView, GetCurrentUserAPIView

urlpatterns = [
    path('user/create',CreateUserAPIView.as_view(),name='create_user'),
    path('user/current', GetCurrentUserAPIView.as_view(), name='current_user'),
    path('user/<int:pk>',GetIDUserAPIView.as_view(), name='get_id_user'),
    path('user/update/<int:pk>',IDUserAPIUpdateView.as_view(),name='id_user_update'),
    path('user/update/current',CurrentUserUpdateAPIView.as_view(),name='current_user_update'),
    path('users/list',UserAPIListView.as_view(),name='user_list'),
]