# Generated by Django 3.1 on 2020-08-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0058_register_activity_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_activity',
            name='publicity_campaign_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]