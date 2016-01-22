# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='location',
            field=models.CharField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='year_created',
            field=models.IntegerField(blank=True),
        ),
    ]
