# Generated by Django 2.2.16 on 2020-10-27 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sift', '0009_auto_20201027_0110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='dish_Category',
            new_name='dish_category',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='dish_Subcategory',
            new_name='dish_subcategory',
        ),
    ]