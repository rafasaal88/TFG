# Generated by Django 2.2.7 on 2020-01-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20200125_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='static/img/profile.png', upload_to='profile_image'),
        ),
    ]