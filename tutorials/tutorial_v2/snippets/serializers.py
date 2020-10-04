# this serializers.py file provide serializing and deserializing the snippet instance into Json
# this file works very similar to the form file in django

from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
