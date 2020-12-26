# Generated by Django 3.0.11 on 2020-12-25 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cardset', '0008_auto_20201225_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='memocardperformance',
            name='learning_timeout',
            field=models.PositiveIntegerField(default=30000, verbose_name='Learning Timeout in ms'),
        ),
    ]