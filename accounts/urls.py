from django.urls import path
from .views import (
    HelloView,
    UserViewSet
)


urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'post'}), name='register'),
    path('hello/', HelloView.as_view({'get': 'get'})),
]