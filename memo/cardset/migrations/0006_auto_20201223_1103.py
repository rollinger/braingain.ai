# Generated by Django 3.0.11 on 2020-12-23 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cardset', '0005_auto_20201223_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memoset',
            old_name='owner',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='memocard',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='Memo Set is owned by this user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memocards', to=settings.AUTH_USER_MODEL),
        ),
    ]
