from django.contrib import admin
from .models import (
    Board,
    BoardInvite,
    BoardMember,
    Card,
    Label,
    List
)

admin.site.register(Board)
admin.site.register(BoardInvite)
admin.site.register(BoardMember)
admin.site.register(Card)
admin.site.register(Label)
admin.site.register(List)