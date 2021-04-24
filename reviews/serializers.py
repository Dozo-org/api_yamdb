from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from .models import Comment, Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    title = serializers.PrimaryKeyRelatedField(read_only=True) #, validators=[UniqueValidator(queryset=Review.objects.all())])

    class Meta:
        fields = '__all__'
        model = Review
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Review.objects.all(),
        #         fields=['author', 'title'],
        #         message='It is impossible to create a 2nd review.',
        #     )
        # ]
    
    # def validate(self, data):
    #     if (
    #         self.context['request'].method == 'POST'
    #         and data['author'] == data['title']
    #     ):
    #         raise serializers.ValidationError(
    #             'Err'
    #         )
    #     return data




class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=Comment.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
