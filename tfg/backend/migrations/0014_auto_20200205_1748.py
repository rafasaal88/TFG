# Generated by Django 2.2.7 on 2020-02-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_auto_20200203_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(),
        ),
    ]
