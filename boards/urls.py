from django.urls import path
from .views import (
  BoardViewSet
)


urlpatterns = [
    path('board/', BoardViewSet.as_view({
      'post': 'post',
      'put': 'put',
      })),
    path('board/<slug:slug>/', BoardViewSet.as_view({
      'get': 'retrieve',
    }))
]