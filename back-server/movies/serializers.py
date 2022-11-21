from rest_framework import serializers
from .models import Movie, Comment
from django.contrib.auth import get_user_model


class MovieListSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview')
        # fields = ('id', 'title', 'overview', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'username', 'movie', 'content', 'score')
        read_only_fields = ('movie', 'username', 'user')
        # extra_kwargs = {'user': {'required': False}}

    


class MovieSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('user', 'like_user')


# class CommentListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = get_user_model()
#             fields = ('pk', 'username')
    
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = ('pk', 'content', 'user', 'created_at', 'updated_at', 'movie', 'score')


