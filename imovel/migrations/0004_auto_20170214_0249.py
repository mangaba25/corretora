# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-14 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0003_auto_20170213_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='book_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Venda'), (2, 'Aluguel')]),
        ),
    ]
