# Generated by Django 5.1.4 on 2024-12-26 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_remove_weather_user_weather_chance_of_rain_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='chance_of_rain',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='forecast',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='history',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='uv_index',
        ),
    ]
