# Generated by Django 3.0.3 on 2020-05-14 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0042_point_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
