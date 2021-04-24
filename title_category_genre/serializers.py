from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Avg
from reviews.models import Review

from .models import Title, Genre, Category


User = get_user_model()

class TitleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    genre = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = '__all__'
    
    def get_rating(self, obj):
        average = Review.objects.all().aggregate(Avg('score')).get('score__avg')
        if average is None:
            return 0
        return average



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
