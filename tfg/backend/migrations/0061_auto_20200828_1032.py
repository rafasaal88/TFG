# Generated by Django 3.1 on 2020-08-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0060_auto_20200827_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_activity',
            name='product_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register_activity',
            name='product_price',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
