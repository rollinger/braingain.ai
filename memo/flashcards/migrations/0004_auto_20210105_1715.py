# Generated by Django 3.0.11 on 2021-01-05 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_auto_20210105_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='topic',
            field=models.ForeignKey(blank=True, help_text='Card is grouped by this topic (optional)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='flashcards.Topic'),
        ),
    ]
