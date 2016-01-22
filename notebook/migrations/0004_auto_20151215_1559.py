# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_auto_20151212_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='country_created',
            field=models.ForeignKey(blank=True, to='notebook.Country', null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='giver',
            field=models.ForeignKey(related_name='giver', blank=True, to='notebook.Creator', null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='object_creator',
            field=models.ForeignKey(blank=True, to='notebook.Creator', null=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='receiver',
            field=models.ForeignKey(related_name='receiver', blank=True, to='notebook.Creator', null=True),
        ),
    ]
