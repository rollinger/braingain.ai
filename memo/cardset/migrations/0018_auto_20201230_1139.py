# Generated by Django 3.0.11 on 2020-12-30 10:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardset', '0017_auto_20201229_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memocard',
            name='answer_text',
            field=ckeditor.fields.RichTextField(max_length=2000, verbose_name='Answer (Text)'),
        ),
    ]
