from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import PageNumberPagination
from users.permission import IsAdminOrReadOnly

from .filters import TitleFilter
from .models import Category, Genre, Title
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleReadOnlySerializer, TitleWriteSerializer)


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleWriteSerializer
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('-id')
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsSuperuserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleWriteSerializer
        return TitleReadOnlySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsSuperuserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsSuperuserOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
