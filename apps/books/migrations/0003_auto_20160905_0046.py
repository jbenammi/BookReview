# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 07:46
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20160904_2122'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('book_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
