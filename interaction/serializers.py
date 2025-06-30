from .models import Like, Bookmark, Comment
from rest_framework import serializers


class LikeSerializer():
    class Meta:
        model = Like
        fields = []

class BookmarkSerializer():
    class Meta:
        model = Bookmark
        fields = []


class CommentSerializer(): 
    class Meta:
        model = Comment
        fields = []  