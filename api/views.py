from django.shortcuts import render
from Posts.models import Model
from .serializers import PostSerializer
from rest_framework import generics
# Create your views here.
from .permissions import IsAuthorized

from rest_framework import viewsets
class ListPosts(viewsets.ModelViewSet):
    permission_classes = (IsAuthorized,)
    queryset = Model.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = (IsAuthorized,)
        queryset = Model.objects.all()
        serializer_class = PostSerializer

