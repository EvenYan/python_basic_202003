# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-28 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='passwd',
            field=models.CharField(default='root', max_length=40),
        ),
    ]
