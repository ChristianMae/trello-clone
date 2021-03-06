from django.shortcuts import get_object_or_404, redirect
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from accounts.models import User
from django.template.defaultfilters import slugify
from .mixins import RequiredBoardMemberMixin
from .models import (
    Board,
    BoardInvite,
    List
)
from .serializers import (
    BoardInviteSerializer,
    BoardMemberSerializer,
    BoardSerializer,
    CardSerializer,
    LabelSerializer,
    ListSerializer,
)
from .utils import (
    get_object_or_none,
    random_str_generator
)


class BoardViewSet(ViewSet):
    """
    Board viewset.
    """
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve_boards(self, *args, **kwargs):
        serializer = self.serializer_class(
            self.serializer_class.Meta.model.objects.filter(owner=self.request.user, archived=False),
            many=True
        )
        return Response(serializer.data, status=200)

    def post(self, *arg, **kwargs):
        "Create board"
        title = self.request.data.get('title', None)
        data = {'title': title, 'slug': self.generate_unique_slug(title=title)}
        serializer = self.serializer_class(data=data, context={'user': self.request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)

    def generate_unique_slug(self, title):
        while True:
            slug = slugify(f'{random_str_generator()} {title}')
            try:
                Board.objects.get(slug=slug)
            except Board.DoesNotExist:
                return slug

    def put(self, *args, **kwargs):
        " Update board details. "
        board_slug = self.request.data.get('slug')
        board = self.serializer_class.Meta.model.objects.get(slug=board_slug)
        serializer = self.serializer_class(
            board,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=400)

    def retrieve(self, *args, **kwargs):
        " Retrieve "
        slug = kwargs.get('slug', None)
        board = get_object_or_404(self.serializer_class.Meta.model, slug=slug)

        serializer = self.serializer_class(board)
        return Response( status=200)


class BoardInviteViewSet(RequiredBoardMemberMixin, ViewSet):
    """
    View for sending invite.
    """
    serializer_class = BoardInviteSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(
            data=self.request.data,
            context={
                'board_member': self.get_member_instance(kwargs.get('slug')),
                'request': self.request
                }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)


class BoardMemberViewSet(ViewSet):
    """
    Accept incoming invitation links.
    """
    serializer_class = BoardMemberSerializer

    def get(self, *args, **kwargs):
        invitation = get_object_or_none(BoardInvite, **kwargs)
        is_user = get_object_or_none(User, email=invitation.email)
        if not is_user:
            return redirect('register')
        return redirect('token_obtain_pair')

    def put(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        # board = get_object_or_none(Board,)
        # user =
        # member = get_object_or_none(
        #     self.serializer_class.Meta.model,
        #     board=,
        #     user=)
        serializer = self.serializer_class(data=self.request.data)
        pass


class ListViewSet(ViewSet):
    """
    Viewset for List
    """
    serializer_class = ListSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data, context=kwargs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def put(self, *args, **kwargs):
        _list_id = self.request.data.get('id')
        _list = get_object_or_none(self.serializer_class.Meta.model, id=_list_id)
        serializer = self.serializer_class(
            _list,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def retrieve(self, *args, **kwargs):
        serializer = self.serializer_class(
            self.serializer_class.Meta.model.objects.filter(board__slug= kwargs.get('slug', None)),
            many=True
        )
        return Response(serializer.data, status=200)


class CardViewSet(ViewSet):
    """
    Viewset for Card
    """

    serializer_class = CardSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, *args, **kwargs):
        _list = get_object_or_none(List, id=kwargs.get('list'))
        serializer = self.serializer_class(
            data=self.request.data,
            context={'board_list': _list}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def put(self, *args, **kwargs):
        card = get_object_or_none(
            self.serializer_class.Meta.model,
            slug=kwargs.get('card_slug')
        )
        serializer = self.serializer_class(
            card,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def retrieve(self, *args, **kwargs):
        " Retrieve "
        slug = kwargs.get('card_slug', None)
        card = get_object_or_404(self.serializer_class.Meta.model, slug=slug)

        serializer = self.serializer_class(card)
        return Response(serializer.data, status=200)

    def retrieve_cards(self, *args, **kwargs):
        serializer = self.serializer_class(
            self.serializer_class.Meta.model.objects.filter(
                board_list__id= kwargs.get('list', None),
                archived=False
                ),
            many=True
        )
        return Response(serializer.data, status=200)


class LabelViewSet(ViewSet):

    serializer_class = LabelSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def put(self, *args, **kwargs):
        label = get_object_or_none(
            self.serializer_class.Meta.model,
            id=kwargs.get('id')
        )
        serializer = self.serializer_class(
            label,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)
