# Generated by Django 3.0.11 on 2021-05-03 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareholder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Task: ...', max_length=255, verbose_name='Short Summary'),
        ),
    ]