# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=100)),
                ('highlighted', models.TextField()),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
