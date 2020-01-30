# Generated by Django 2.2.7 on 2020-01-25 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200110_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='admin_company',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]