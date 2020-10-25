import random
import datetime

from django.core.management.base import BaseCommand

from ...models import Difficulty, Cuisine, UOM, Grocery, Cookware


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
    UOM.objects.get_or_create(measurement='teaspoon')
    UOM.objects.get_or_create(measurement='tablespoon')
    UOM.objects.get_or_create(measurement='fluid ounce')
    UOM.objects.get_or_create(measurement='gill')
    UOM.objects.get_or_create(measurement='cup')
    UOM.objects.get_or_create(measurement='pint')
    UOM.objects.get_or_create(measurement='quart')
    UOM.objects.get_or_create(measurement='gallon')
    UOM.objects.get_or_create(measurement='ml')
    UOM.objects.get_or_create(measurement='l')
    UOM.objects.get_or_create(measurement='dl')
    UOM.objects.get_or_create(measurement='pound')
    UOM.objects.get_or_create(measurement='ounce')
    UOM.objects.get_or_create(measurement='mg')
    UOM.objects.get_or_create(measurement='g')
    UOM.objects.get_or_create(measurement='kg')
    UOM.objects.get_or_create(measurement='mm')
    UOM.objects.get_or_create(measurement='cm')
    UOM.objects.get_or_create(measurement='m')
    UOM.objects.get_or_create(measurement='inch')
    UOM.objects.get_or_create(measurement='can')


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


class Command(BaseCommand):
    help = 'Populates Database with initial data.'

    def handle(self, *args, **options):
        populate_difficulty()
        populate_cuisine()
        populate_uom()
        populate_grocery()
        populate_cookware()
