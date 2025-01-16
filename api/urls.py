from django.urls import path
from django.views.generic import RedirectView
from .views import UserViewSet

urlpatterns = [
    path('', RedirectView.as_view(url='users/')),  # Redireciona api/ para api/users/
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]