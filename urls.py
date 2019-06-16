from django.db import models
from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response

from views import about, index


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)

class PostViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Post.objects.all()

    def list(self, request):
        resp = Response({"blub": "list"})
        return resp

post_list = PostViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('', index),
    path('about', about),
    path('api/posts/', post_list),
]
