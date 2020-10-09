from django.contrib import admin
from .models import Difficulty, Genre, UOM, Amount, Grocery, Ingredients, Cookware, Recipe

# Register your models here.


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ('type_txt',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('type_txt',)


@admin.register(UOM)
class UOMAdmin(admin.ModelAdmin):
    list_display = ('measurement',)


@admin.register(Amount)
class AmountAdmin(admin.ModelAdmin):
    list_display = ('number', 'uom')


@admin.register(Grocery)
class GroceryAdmin(admin.ModelAdmin):
    list_display = ('type_txt',)


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('grocery', 'amount', 'name')


@admin.register(Cookware)
class CookwareAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
