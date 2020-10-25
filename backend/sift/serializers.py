from .models import Recipe
from rest_framework import serializers


class RecipesSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)
    main_image_url = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description',
                  'total_time', 'difficulty', 'cuisine', 'main_image_url']


class RecipeSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)
    cookware = serializers.StringRelatedField(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
