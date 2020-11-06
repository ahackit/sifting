from rest_framework import serializers

from .models import Recipe, Step, UOM, Ingredients, Amount, Grocery


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = '__all__'


class RecipeListSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many=False)
    cuisine = serializers.StringRelatedField(many=False)
    main_image_url = serializers.CharField(read_only=True)
    dish_category = serializers.StringRelatedField(many=False)
    dish_subcategory = serializers.StringRelatedField(many=False)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description',
                  'total_time', 'difficulty', 'cuisine', 'main_image_url', 'dish_category', 'dish_subcategory']


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


class AmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amount
        fields = '__all__'


class GrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocery
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    amount = AmountSerializer(many=False)
    grocery = GrocerySerializer(many=False)

    class Meta:
        model = Ingredients
        fields = '__all__'


class RecipeGroceryListSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['ingredients']
