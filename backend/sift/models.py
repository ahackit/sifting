from django.db import models

# Create your models here.


class Difficulty(models.Model):
    type_txt = models.CharField(max_length=50)

    def __str__(self):
        return self.type_txt


class Cuisine(models.Model):
    type_txt = models.CharField(max_length=50)

    def __str__(self):
        return self.type_txt


class UOM(models.Model):
    measurement = models.CharField(max_length=20)

    def __str__(self):
        return self.measurement


class Amount(models.Model):
    number = models.IntegerField()
    uom = models.ForeignKey("UOM", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.number} {self.uom.measurement}'


class Grocery(models.Model):
    type_txt = models.CharField(max_length=50)

    def __str__(self):
        return self.type_txt


class Ingredients(models.Model):
    grocery = models.ForeignKey(
        "Grocery", on_delete=models.SET_NULL, null=True)
    amount = models.ForeignKey("Amount", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.amount}'


class Cookware(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def raw_image_path(instance, filename):
    return f'recipes/{instance.id}/{filename}'


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    prep_time = models.IntegerField()
    total_time = models.IntegerField()
    main_image = models.ImageField(upload_to=raw_image_path, null=True)
    difficulty = models.ForeignKey(
        "Difficulty", on_delete=models.SET_NULL, null=True)
    cuisine = models.ForeignKey(
        "Cuisine", on_delete=models.SET_NULL, null=True)
    cookware = models.ManyToManyField("Cookware")
    ingredients = models.ManyToManyField("Ingredients")

    def main_image_url(self):
        if self.main_image:
            return self.main_image.url
        return ''
