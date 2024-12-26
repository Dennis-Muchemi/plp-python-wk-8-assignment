# Generated by Django 5.1.4 on 2024-12-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weather_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='user',
        ),
        migrations.AddField(
            model_name='weather',
            name='chance_of_rain',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='forecast',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='history',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weather',
            name='uv_index',
            field=models.FloatField(blank=True, null=True),
        ),
    ]