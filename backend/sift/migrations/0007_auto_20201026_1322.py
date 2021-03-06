# Generated by Django 2.2.16 on 2020-10-26 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sift', '0006_step'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_txt', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='calories_per_serving',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Dish_Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_txt', models.CharField(max_length=255)),
                ('dish_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sift.Dish_Category')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='Dish_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sift.Dish_Category'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='Dish_Subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sift.Dish_Subcategory'),
        ),
    ]
