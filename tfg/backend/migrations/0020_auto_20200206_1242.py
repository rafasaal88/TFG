# Generated by Django 2.2.7 on 2020-02-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_product_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, null=True),
        ),
    ]