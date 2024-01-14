from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from app_jlims.models import Library


class UserSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

"""
class LibrarySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Library
            fields = ['publisher', 'author', 'title', 'pageCount', 'category', 'shelfLocation', 'publishedDate', 'isInStock', 'dateCheckedOut']

"""


class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = [f.name for f in model._meta.fields]