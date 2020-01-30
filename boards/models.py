from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User


class Board(models.Model):
    """
    Model for board.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    archived = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    title = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f'{self.title}'


class BoardMember(models.Model):
    """
    Model for board member.
    """
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'


class BoardInvite(models.Model):
    """
    Model for Board Member invite.
    """
    board_member = models.ForeignKey(
        BoardMember,
        on_delete=models.CASCADE
    )
    email = models.EmailField(max_length=255)
    token = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.board_member} sent an invite to {self.email}'


class List(models.Model):
    """
    List in specific board.
    """
    archived = models.BooleanField(default=False)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.board.title} - {self.title}'


class Card(models.Model):
    """
    Models for card.
    """
    archived = models.BooleanField(default=False)
    board_list = models.ForeignKey(
        List,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    due_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.board_list.board.title}: {self.board_list.title} - {self.title}'


class CardMember(models.Model):
    board_member = models.ForeignKey(
        BoardMember,
        on_delete=models.CASCADE
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.card.name}-{self.board_member.user}'


class Label(models.Model):
    name = models.CharField(max_length=100)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CardLabel(models.Model):
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE
    )
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.card} - {self.label.name}'

# Signals
@receiver(post_save, sender=Board)
def create_member(sender, instance, created, **kwargs):
    if created:
        BoardMember.objects.create(
            board=instance,
            user=instance.owner,
            is_admin=True
        )
