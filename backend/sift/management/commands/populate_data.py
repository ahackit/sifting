import random
import datetime

from django.core.management.base import BaseCommand

from ...models import Difficulty, Cuisine, UOM, Grocery, Cookware, Dish_Category, Dish_Subcategory


def populate_difficulty():
    Difficulty.objects.get_or_create(type_txt='Easy')
    Difficulty.objects.get_or_create(type_txt='Medium')
    Difficulty.objects.get_or_create(type_txt='Hard')


def populate_cuisine():
    Cuisine.objects.get_or_create(type_txt='Mexican')
    Cuisine.objects.get_or_create(type_txt='Italian')
    Cuisine.objects.get_or_create(type_txt='American')
    Cuisine.objects.get_or_create(type_txt='Chinese')
    Cuisine.objects.get_or_create(type_txt='Thai')
    Cuisine.objects.get_or_create(type_txt='Greek')
    Cuisine.objects.get_or_create(type_txt='Indian')


def populate_uom():
    UOM.objects.get_or_create(measurement='teaspoon',
                              conversion_type='volume', multiplier=5)
    UOM.objects.get_or_create(measurement='tablespoon',
                              conversion_type='volume', multiplier=15)
    UOM.objects.get_or_create(
        measurement='cup', conversion_type='volume', multiplier=237)
    UOM.objects.get_or_create(
        measurement='pint', conversion_type='volume', multiplier=473)
    UOM.objects.get_or_create(
        measurement='quart', conversion_type='volume', multiplier=946)
    UOM.objects.get_or_create(measurement='gallon',
                              conversion_type='volume', multiplier=3800)
    UOM.objects.get_or_create(
        measurement='ml', conversion_type='volume', multiplier=.2)
    UOM.objects.get_or_create(
        measurement='l', conversion_type='volume', multiplier=1000)
    UOM.objects.get_or_create(
        measurement='ounce', conversion_type='weight', multiplier=28)
    UOM.objects.get_or_create(
        measurement='pound', conversion_type='weight', multiplier=454)
    UOM.objects.get_or_create(
        measurement='g', conversion_type='weight', multiplier=.035)


def populate_grocery():
    Grocery.objects.get_or_create(type_txt='beverages')
    Grocery.objects.get_or_create(type_txt='bakery')
    Grocery.objects.get_or_create(type_txt='canned good')
    Grocery.objects.get_or_create(type_txt='dairy')
    Grocery.objects.get_or_create(type_txt='dry/baking good')
    Grocery.objects.get_or_create(type_txt='frozen foods')
    Grocery.objects.get_or_create(type_txt='produce')


def populate_cookware():

    Cookware.objects.get_or_create(name="stock pot")
    Cookware.objects.get_or_create(name="frying pan")
    Cookware.objects.get_or_create(name="cast iron skillet")
    Cookware.objects.get_or_create(name="saute pan")
    Cookware.objects.get_or_create(name="Sauce pan")
    Cookware.objects.get_or_create(name="slower cooker")
    Cookware.objects.get_or_create(name="roasting pan")
    Cookware.objects.get_or_create(name="dutch oven")


def populate_categories():
    dish, _ = Dish_Category.objects.get_or_create(type_txt='main')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='cheesy')
    Dish_Subcategory.objects.get_or_create(dish_category=dish, type_txt='meat')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='poultry')
    Dish_Subcategory.objects.get_or_create(dish_category=dish, type_txt='fish')
    Dish_Subcategory.objects.get_or_create(dish_category=dish, type_txt='eggs')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='vegetarian')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='game day')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='breakfast')

    dish, _ = Dish_Category.objects.get_or_create(type_txt='side')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='vegetables')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='potatoes')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='grains')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='salad')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='lentils')
    Dish_Subcategory.objects.get_or_create(
        dish_category=dish, type_txt='bread')


class Command(BaseCommand):
    help = 'Populates Database with initial data.'

    def handle(self, *args, **options):
        populate_difficulty()
        populate_cuisine()
        populate_uom()
        populate_grocery()
        populate_cookware()
        populate_categories()
