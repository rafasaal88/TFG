# Generated by Django 3.0.3 on 2020-05-14 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0044_auto_20200514_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='point',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
