from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import reverse
from rest_framework import serializers
from uuid import uuid4
from .models import (
    Board,
    BoardInvite,
    BoardMember,
    Card,
    CardLabel,
    Label,
    List
)
from .utils import (
    get_object_or_none,
    random_str_generator
)


class BoardSerializer(serializers.ModelSerializer):
    """
    Board Serializer.
    """

    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'archived',
            'slug'
        ]

    def create(self, validated_data):
        title = validated_data.get('title')
        board = self.Meta.model.objects.create(
            slug = self.generate_unique_slug(title),
            owner = self.context['user'],
            **validated_data
        )
        return board

    def generate_unique_slug(self, title):
        while True:
            slug = slugify(f'{random_str_generator()} {title}')
            try:
                self.Meta.model.objects.get(slug=slug)
            except self.Meta.model.DoesNotExist:
                return slug

    def update(self, instance, validated_data):
        instance.archived = validated_data.get('archived', instance.archived)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class BoardInviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardInvite
        fields = [
            'email',
        ]

    def validate(self, data):
        " Clean invited email "
        email = data.get('email')
        is_owner = get_object_or_none(Board, owner__email=email)
        is_member = get_object_or_none(BoardMember, user__email=email)

        if is_owner or is_member:
            raise serializers.ValidationError('Already a member.')

        return data

    def create(self, validated_data):
        " Create invitation "
        token = self.generate_token()
        board_member = self.context['board_member']
        member = self.Meta.model.objects.create(
            board_member=board_member,
            token=token,
            **validated_data
        )
        self.send_invitation(token=self.generate_token())
        return member

    def generate_token(self):
        not_found = True
        while not_found:
            token = uuid4().hex
            try:
                self.Meta.model.objects.get(token=token)
            except self.Meta.model.DoesNotExist:
                not_found = False
                return token

    def send_invitation(self, token, *args, **kwargs):
        " Send email invitation to join board."
        member = self.context['board_member']
        request = self.context['request']
        email = self.validated_data.get('email')
        urlpattern = reverse('invitation-link', kwargs={'token': token})
        invitation_link = request.build_absolute_uri(urlpattern)
        message = f'{member.user}, has invited you to join {member.board} board. To join the board click the link {invitation_link}.'

        send_mail(
            'Invitation to join board.',
            message,
            settings.EMAIL_HOST_USER,
            [email, ],
            fail_silently=False,
        )


class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = ['is_admin']

    def create(self, validated_data):
        invitation_instance = get_object_or_none(BoardInvite, token=self.context['token'])
        board = invitation_instance.board_member.board,
        member = self.Meta.models.object.create(
            board = board,
            user = invitation_instance.board_member.user
        )
        return member


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ['title']

    def create(self, validated_data):
        board = get_object_or_none(Board, **self.context)
        _list = self.Meta.model.objects.create(board=board, **validated_data)
        return _list

    def update(self, instance, validated_data):
        instance.archived = validated_data.get('archived', instance.archived)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            'title',
            'description'
        ]

    def create(self, validated_data):
        title = validated_data['title']
        card = self.Meta.model.objects.create(
            **validated_data,
            **self.context,
            slug=self.generate_unique_slug(title)
        )
        return card

    def generate_unique_slug(self, title):
        while True:
            slug = slugify(f'{random_str_generator()} {title}')
            try:
                self.Meta.model.objects.get(slug=slug)
            except self.Meta.model.DoesNotExist:
                return slug

    def update(self, instance, validated_data):
        instance.archived = validated_data.get('archived', instance.archived)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.title)
        instance.board_list = self.context.get('board_list', instance.board_list)
        instance.save()
        return instance


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = [
            'name',
            'is_archived'
        ]

    def create(self, validated_data):
        label = self.Meta.model.objects.create(**validated_data)
        return label

    def udpated(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.is_archived = validated_data.get('is_archived', instance.is_archived)
        instance.save()
        return instance


class CardLabelSerializer(serializers.ModelSerializer):

    class Meta:
        models = CardLabel
        fields = ['card']
