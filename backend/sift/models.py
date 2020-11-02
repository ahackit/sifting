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
    conversion_type = models.CharField(max_length=50, null=True)
    multiplier = models.FloatField(null=True)

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['measurement'],  name='unique_measurement_name')]

    def convert_to(self, start_uom_numer, end_uom_txt):
        first_to_ml = self.multiplier * float(start_uom_numer)
        return round(first_to_ml / UOM.objects.get(measurement=end_uom_txt).multiplier, 4)

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


class Step(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    note = models.CharField(max_length=500, null=True, blank=True)


class Dish_Category(models.Model):
    type_txt = models.CharField(max_length=255)

    def __str__(self):
        return self.type_txt


class Dish_Subcategory(models.Model):
    dish_category = models.ForeignKey(
        "Dish_Category", on_delete=models.CASCADE)
    type_txt = models.CharField(max_length=255)

    def __str__(self):
        return self.type_txt


def raw_image_path(instance, filename):
    return f'recipes/{instance.id}/{filename}'


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    prep_time = models.IntegerField()
    total_time = models.IntegerField()
    servings = models.IntegerField(null=True)
    calories_per_serving = models.IntegerField(null=True)
    main_image = models.ImageField(upload_to=raw_image_path, null=True)
    dish_category = models.ForeignKey(
        "Dish_Category", on_delete=models.SET_NULL, null=True)
    dish_subcategory = models.ForeignKey(
        "Dish_Subcategory", on_delete=models.SET_NULL, null=True)
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

    def steps(self):
        return Step.objects.filter(recipe=self)
