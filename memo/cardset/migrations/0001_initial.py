# Generated by Django 3.0.11 on 2020-12-21 09:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemoSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lft', models.PositiveIntegerField(db_index=True)),
                ('rgt', models.PositiveIntegerField(db_index=True)),
                ('tree_id', models.PositiveIntegerField(db_index=True)),
                ('depth', models.PositiveIntegerField(db_index=True)),
                ('topic', models.CharField(help_text='Topic of Memo Card', max_length=255, verbose_name='Topic')),
                ('owner', models.ForeignKey(blank=True, help_text='Memo Set is owned by this user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memosets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Set',
                'verbose_name_plural': 'Sets',
            },
        ),
        migrations.CreateModel(
            name='MemoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('topic', models.CharField(help_text='Topic of Memo Card', max_length=255, verbose_name='Topic')),
                ('question_text', models.TextField(max_length=2000, verbose_name='Question (Text)')),
                ('answer_text', models.TextField(max_length=2000, verbose_name='Answer (Text)')),
                ('data', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Memorization Data')),
                ('score', models.DecimalField(decimal_places=1, default=0.0, help_text='Memorization Score of the Memo Card', max_digits=4, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Memorization Score')),
                ('memoset', models.ForeignKey(help_text='Memo Card is assigned to this set', on_delete=django.db.models.deletion.CASCADE, related_name='memocards', to='cardset.MemoSet')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
    ]
