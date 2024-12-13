from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response

from blog.models import Author
from blog.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

