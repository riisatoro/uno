# Generated by Django 3.2 on 2021-04-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_game_player_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='has_left',
            field=models.BooleanField(default=False),
        ),
    ]
