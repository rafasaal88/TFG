# Generated by Django 2.2.7 on 2020-02-03 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20200203_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=None),
        ),
    ]
