# Generated by Django 3.0.3 on 2020-02-14 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]