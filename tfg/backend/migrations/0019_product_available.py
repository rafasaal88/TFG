# Generated by Django 2.2.7 on 2020-02-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
