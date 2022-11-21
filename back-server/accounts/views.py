from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserDetailSerializer
from movies.serializers import CommentSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def user_comments(user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    comments = user.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)