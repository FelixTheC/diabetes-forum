# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-04 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=254, null=True)),
                ('discription', models.TextField(null=True)),
                ('bePerPortion', models.IntegerField(null=True)),
            ],
        ),
    ]
