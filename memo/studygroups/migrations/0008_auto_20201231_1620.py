# Generated by Django 3.0.11 on 2020-12-31 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0007_auto_20201231_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studygroup',
            options={'ordering': ('-is_main_user_group', 'name'), 'verbose_name': 'Study Group', 'verbose_name_plural': 'Study Groups'},
        ),
    ]
