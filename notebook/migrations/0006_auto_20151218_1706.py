# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_auto_20151215_1601'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Place',
        ),
        migrations.RenameField(
            model_name='creator',
            old_name='creator_country',
            new_name='creator_home',
        ),
        migrations.RenameField(
            model_name='object',
            old_name='country_created',
            new_name='place_created',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='country_name',
            new_name='place_name',
        ),
    ]
