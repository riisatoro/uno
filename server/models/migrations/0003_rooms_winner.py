# Generated by Django 3.2 on 2021-04-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20210410_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]
