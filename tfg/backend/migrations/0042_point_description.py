# Generated by Django 3.0.3 on 2020-03-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_tag_nfc_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='description',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
