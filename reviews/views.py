from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Review, Comment, User


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    #permission_classes = (IsAuthenticatedOrReadOnly, )


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
   # permission_classes = (IsAuthenticatedOrReadOnly, )
  

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        return review.comments.all()



