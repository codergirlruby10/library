from rest_framework import viewsets, permissions
from rest_framework.response import Response
from catalog.models import Author, Book
from catalog.api.serializers import AuthorSerializer, BookSerializer
from django_filters import rest_framework as filters
from catalog.filters import BookFilter

#1. Define the viewset as a model view viewset
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
