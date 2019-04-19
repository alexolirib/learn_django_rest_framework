# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-19 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('idCarro', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('modeloCarro', models.CharField(db_column='MODELO', max_length=50)),
                ('marcaCarro', models.CharField(db_column='MARCA', max_length=50)),
                ('anoCarro', models.IntegerField(db_column='ANO')),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
    ]
