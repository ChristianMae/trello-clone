from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response

from .serializers import (
    UserSerializer
)


class UserViewSet(ModelViewSet):
    """
    User registration/signup view.
    """
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)


class HelloView(ViewSet):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
