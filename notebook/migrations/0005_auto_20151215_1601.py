# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20151215_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='year_created',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
