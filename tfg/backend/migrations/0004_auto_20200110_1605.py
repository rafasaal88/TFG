# Generated by Django 2.2.7 on 2020-01-10 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200108_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicity_campaign',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]