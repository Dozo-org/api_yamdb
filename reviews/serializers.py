from rest_framework import serializers

from .models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comments = serializers.SlugRelatedField(
    #     queryset = Comment.objects.all(),
    #     slug_field='title_id',
    #     default=None
    # )

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.PrimaryKeyRelatedField(
        queryset = Comment.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Comment

