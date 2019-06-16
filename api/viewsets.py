from django.urls import path
from rest_framework import viewsets
from rest_framework.response import Response

from views import about, index

class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        resp = Response({"blub": "list"})
        return resp

