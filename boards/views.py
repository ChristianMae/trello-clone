from django.shortcuts import get_object_or_404
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from .serializers import (
    BoardSerializer,
)


class BoardViewSet(ViewSet):
    """
    Board viewset.
    """
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, *arg, **kwargs):
        "Create board"
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def put(self, *args, **kwargs):
        " Update board details. "
        board_id = self.request.data.get('id')
        board = self.serializer_class.Meta.model.objects.get(id=board_id)
        serializer = self.serializer_class(board, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def retrieve(self, *args, **kwargs):
        " Retrieve "
        slug = kwargs.get('slug', None)
        board = get_object_or_404(self.serializer_class.Meta.model, slug=slug)

        serializer = self.serializer_class(board)
        return Response(serializer.data, status=200)


