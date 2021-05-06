# Generated by Django 3.0.11 on 2021-05-06 13:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shareholder', '0005_auto_20210504_1157'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together={('task', 'collaborator')},
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('task', 'reviewer')},
        ),
    ]
