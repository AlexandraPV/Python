# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.IntegerField()),
                ('show_n', models.BooleanField(default=False)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cinema.City'),
        ),
        migrations.AddField(
            model_name='cinema',
            name='seance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cinema.Seance'),
        ),
    ]