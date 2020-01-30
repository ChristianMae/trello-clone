from django.urls import path
from .views import (
  BoardInviteViewSet,
  BoardViewSet,
  BoardMemberViewSet,
  CardViewSet,
  LabelViewSet,
  ListViewSet
)


urlpatterns = [
    path('boards/', BoardViewSet.as_view({
      'get': 'retrieve_boards',
    })),
    path('board/list/', ListViewSet.as_view({
      'put': 'put',
    })),
    path('board/', BoardViewSet.as_view({
      'post': 'post',
    })),
    path('board/invitation/<str:token>/', BoardMemberViewSet.as_view({
      'get': 'get',
    }), name='invitation-link'),
    path('board/<slug:slug>/', BoardViewSet.as_view({
      'get': 'retrieve',
      'put': 'put',
    })),
    path('board/<slug:slug>/invite/', BoardInviteViewSet.as_view({
      'post': 'post',
    })),
    path('board/<slug:slug>/list/', ListViewSet.as_view({
      'post': 'post',
      'get': 'retrieve',
    })),
    path('board/<int:list>/card/', CardViewSet.as_view({
      'post': 'post',
      'get': 'retrieve_cards',
    })),
    path('board/<slug:board_slug>/list/<slug:card_slug>/', CardViewSet.as_view({
      'get': 'retrieve',
      'put': 'put',
    })),
    path('label/', LabelViewSet.as_view({
      'post': 'post',
    })),
    path('label/<int:id>/', LabelViewSet.as_view({
      'put': 'put',
    })),
]