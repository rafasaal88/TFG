# Generated by Django 3.0.3 on 2020-08-25 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0054_auto_20200824_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag_nfc',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tag_nfc',
            name='user',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
