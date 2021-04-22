from rest_framework import serializers

from .models import Review, Comment, User, Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True)
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # comments = serializers.SlugRelatedField(
    #     queryset = Comment.objects.all(),
    #     slug_field='title_id',
    #     default=None
    # )

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    # review = serializers.PrimaryKeyRelatedField(read_only=True)
    review = serializers.PrimaryKeyRelatedField(
        queryset = Comment.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Comment

