# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160905_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='_author',
            new_name='fk_author',
        ),
    ]
