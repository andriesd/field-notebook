# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_auto_20151211_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='country_created',
            field=models.ForeignKey(to='notebook.Country', blank=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='object_creator',
            field=models.ForeignKey(to='notebook.Creator', blank=True),
        ),
    ]
