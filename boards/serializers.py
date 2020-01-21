from django.template.defaultfilters import slugify
from rest_framework import serializers
from .models import (
    Board,
    BoardMember,
    List,
)
from .utils import random_str_generator


class BoardSerializer(serializers.ModelSerializer):
    """
    Board Serializer.
    """

    class Meta:
        model = Board
        fields = ['id', 'title', 'archived']

    def create(self, validated_data):
        title = validated_data.get('title')
        validated_data.update({'slug':self.generate_unique_slug(title)})
        board = self.Meta.model.objects.create(**validated_data)
        return board

    def generate_unique_slug(self, title):
        while True:
            slug = slugify(f'{random_str_generator()} {title}')
            try:
                self.Meta.model.objects.get(slug=slug)
            except Board.DoesNotExist:
                return slug

    def update(self, instance, validated_data):
        instance.archived = validated_data.get('archived', instance.archived)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance


class BoardMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardMember
        field = ['id', 'title', 'archived']
