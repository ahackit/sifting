from rest_framework import serializers

from .models import Recipe, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class RecipeListSerializer(serializers.ModelSerializer):
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
    dish_category = serializers.StringRelatedField(many=False)
    dish_subcategory = serializers.StringRelatedField(many=False)
    steps = StepSerializer(many=True)
    main_image_url = serializers.CharField(read_only=True)

    class Meta:
        model = Recipe
        fields = '__all__'
