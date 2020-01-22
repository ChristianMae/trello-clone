from django.http import Http404
from .models import (
    Board,
    BoardMember
)
from .utils import get_object_or_none

class RequiredBoardMemberMixin():

    def initial(self, *args, **kwargs):
        user = self.request.user
        board = get_object_or_none(Board, slug=kwargs.get('slug'))
        member = get_object_or_none(
            BoardMember,
            user=user,
            board=board
        )
        if not member:
            raise Http404

        return super().initial(*args, **kwargs)


    def get_member_instance(self, slug):
        board = get_object_or_none(Board, slug=slug)
        member = get_object_or_none(
            BoardMember,
            user=self.request.user,
            board=board
        )

        return member
