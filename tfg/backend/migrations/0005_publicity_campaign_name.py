# Generated by Django 2.2.7 on 2020-01-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200110_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicity_campaign',
            name='name',
            field=models.TextField(blank=True),
        ),
    ]