# Generated by Django 3.0.3 on 2020-03-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_recipe_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicity_campaign',
            name='product',
            field=models.ManyToManyField(blank=True, related_name='product', to='backend.Product'),
        ),
    ]
