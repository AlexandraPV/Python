# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='Cinema',
        ),
    ]
