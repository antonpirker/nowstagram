from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response

from views import about, index


class PostViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return []

    def list(self, request):
        resp = Response({"blub": "list"})
        return resp

post_list = PostViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('', index),
    path('about', about),
    path('api/posts/', post_list),
]
