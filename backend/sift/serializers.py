from .models import Recipe
from rest_framework import serializers


class RecipesSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)

    class Meta:
        model = Recipe
        fields = ['title', 'description',
                  'total_time', 'difficulty', 'cuisine']


class RecipeSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)
    cookware = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
