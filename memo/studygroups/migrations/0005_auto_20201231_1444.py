# Generated by Django 3.0.11 on 2020-12-31 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0004_auto_20201231_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='join_mode',
        ),
        migrations.AddField(
            model_name='studygroup',
            name='auto_approve_new_member',
            field=models.BooleanField(default=False, help_text='New members are approved automatically', verbose_name='Automatic Approval'),
        ),
    ]
