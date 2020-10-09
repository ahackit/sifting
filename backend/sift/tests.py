import json
from django.test import TestCase, Client
from .models import *

# Create your tests here.


class RecipeViewTestCase(TestCase):
    def setUp(self):
        Difficulty.objects.create(type_txt='Easy')
        Genre.objects.create(type_txt='Mexican')
        cook = Cookware.objects.create(name='Pan')
        UOM.objects.create(measurement='ounces')
        Amount.objects.create(number=14, uom=UOM.objects.all().first())
        Grocery.objects.create(type_txt='Canned Goods')
        ing = Ingredients.objects.create(grocery=Grocery.objects.all(
        ).first(), amount=Amount.objects.all().first(), name='Pinto Beans')
        recip = Recipe.objects.create(title='Refried Beans', description='Famous beans', prep_time=5, total_time=15,
                                      img_link='', difficulty=Difficulty.objects.all().first(), genre=Genre.objects.all().first())
        recip.ingredients.add(ing)
        recip.cookware.add(cook)

    def test_recipe_list_view_works(self):
        c = Client()

        response = c.get('/recipes/')

        self.assertEqual(response.json()[0]['title'], 'Refried Beans')

    def test_recipe_detail_view_works(self):
        c = Client()

        response = c.get('/recipes/1/')
        self.assertEqual(response.json()['title'], 'Refried Beans')
