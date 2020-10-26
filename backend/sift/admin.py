from django.contrib import admin
from .models import Difficulty, Cuisine, UOM, Amount, Grocery, Ingredients, Cookware, Recipe, Step

# Register your models here.


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ('type_txt',)


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
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


class StepAdmin(admin.StackedInline):
    model = Step


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = [StepAdmin]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step)
