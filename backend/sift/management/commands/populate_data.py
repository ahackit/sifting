import lorem
import random
import datetime

from django.core.management.base import BaseCommand

from ...models import Difficulty, Cuisine, UOM, Grocery, Cookware


def populate_difficulty():
    Difficulty.objects.create(type_txt='Easy')
    Difficulty.objects.create(type_txt='Medium')
    Difficulty.objects.create(type_txt='Hard')


def populate_cuisine():
    Cuisine.objects.create(type_txt='Mexican')
    Cuisine.objects.create(type_txt='Italian')
    Cuisine.objects.create(type_txt='American')
    Cuisine.objects.create(type_txt='Chinese')
    Cuisine.objects.create(type_txt='Thai')
    Cuisine.objects.create(type_txt='Greek')
    Cuisine.objects.create(type_txt='Indian')


def populate_uom():
    UOM.objects.create(measurement='teaspoon')
    UOM.objects.create(measurement='tablespoon')
    UOM.objects.create(measurement='fluid ounce')
    UOM.objects.create(measurement='gill')
    UOM.objects.create(measurement='cup')
    UOM.objects.create(measurement='pint')
    UOM.objects.create(measurement='quart')
    UOM.objects.create(measurement='gallon')
    UOM.objects.create(measurement='ml')
    UOM.objects.create(measurement='l')
    UOM.objects.create(measurement='dl')
    UOM.objects.create(measurement='pound')
    UOM.objects.create(measurement='ounce')
    UOM.objects.create(measurement='mg')
    UOM.objects.create(measurement='g')
    UOM.objects.create(measurement='kg')
    UOM.objects.create(measurement='mm')
    UOM.objects.create(measurement='cm')
    UOM.objects.create(measurement='m')
    UOM.objects.create(measurement='inch')


def populate_grocery():
    Grocery.objects.create(type_txt='beverages')
    Grocery.objects.create(type_txt='bakery')
    Grocery.objects.create(type_txt='canned good')
    Grocery.objects.create(type_txt='dairy')
    Grocery.objects.create(type_txt='dry/baking good')
    Grocery.objects.create(type_txt='frozen foods')
    Grocery.objects.create(type_txt='produce')


def populate_cookware():

    Cookware.objects.create(name="stock pot")
    Cookware.objects.create(name="frying pan")
    Cookware.objects.create(name="cast iron skillet")
    Cookware.objects.create(name="saute pan")
    Cookware.objects.create(name="Sauce pan")
    Cookware.objects.create(name="slower cooker")
    Cookware.objects.create(name="roasting pan")
    Cookware.objects.create(name="dutch oven")


class Command(BaseCommand):
    help = 'Populates Database with initial data.'

    def handle(self, *args, **options):
        populate_difficulty()
        populate_cuisine()
        populate_uom()
        populate_grocery()
        populate_cookware()
