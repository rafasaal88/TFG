# Generated by Django 2.2.7 on 2020-02-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20200205_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
