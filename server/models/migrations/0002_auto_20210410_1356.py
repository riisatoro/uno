# Generated by Django 3.2 on 2021-04-10 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_started', models.BooleanField(default=False)),
                ('is_ended', models.BooleanField(default=False)),
                ('last_card', models.JSONField(null=True)),
                ('started_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_cards', models.JSONField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(through='models.Rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
