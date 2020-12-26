# Generated by Django 3.0.11 on 2020-12-26 09:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardset', '0010_auto_20201225_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memocardperformance',
            name='score',
        ),
        migrations.AddField(
            model_name='memocardperformance',
            name='test_score',
            field=models.DecimalField(decimal_places=1, default=0.0, help_text='Test Score of the Memo Card for the User', max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Test Score'),
        ),
        migrations.AddField(
            model_name='memocardperformance',
            name='test_total_time',
            field=models.PositiveIntegerField(default=0, help_text='Total time spend on testing', verbose_name='Total Test Time'),
        ),
        migrations.AddField(
            model_name='memocardperformance',
            name='train_score',
            field=models.DecimalField(decimal_places=1, default=0.0, help_text='Train Score of the Memo Card for the User', max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Train Score'),
        ),
        migrations.AddField(
            model_name='memocardperformance',
            name='train_total_time',
            field=models.PositiveIntegerField(default=0, help_text='Total time spend on learning', verbose_name='Total Train Time'),
        ),
        migrations.AlterField(
            model_name='memocardperformance',
            name='learning_timeout',
            field=models.PositiveSmallIntegerField(default=30, help_text='Learning Timeout in seconds', verbose_name='Learning Timeout'),
        ),
    ]
