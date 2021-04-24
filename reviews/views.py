from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .permissions import IsAuthorOrReadOnly

from rest_framework.response import Response

from . import serializers
from .models import Review, Comment
from title_category_genre.models import Title


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'post', 'patch', 'delete']

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        # review = get_object_or_404(Review, author=self.request.user)
        # print(review)
        # # print(title)
        # # queryset = Review.objects.filter(author=self.request.user)
        # if review.exists():
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(author=self.request.user, title=title)
 
    
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.review.all()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'post', 'patch', 'delete']
  

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()
