# Generated by Django 3.0.3 on 2020-08-24 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0052_city2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='City2',
        ),
    ]
