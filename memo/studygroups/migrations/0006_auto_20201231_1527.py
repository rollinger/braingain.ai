# Generated by Django 3.0.11 on 2020-12-31 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0005_auto_20201231_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[('viewer', 'Viewer'), ('editor', 'Editor'), ('admin', 'Admin')], default=0, help_text="Member's role in study group", verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='is_publicly_available',
            field=models.BooleanField(default=True, help_text='Study Group can be joined over the directory', verbose_name='Publicly available'),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='new_member_role',
            field=models.CharField(choices=[('viewer', 'Viewer'), ('editor', 'Editor'), ('admin', 'Admin')], default='viewer', help_text='Default role of new member', max_length=20, verbose_name='Default member role'),
        ),
    ]
