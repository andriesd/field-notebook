# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator_name', models.CharField(max_length=150)),
                ('creator_country', models.ForeignKey(to='notebook.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_name', models.CharField(max_length=50)),
                ('year_created', models.IntegerField()),
                ('location', models.CharField(max_length=75)),
                ('location_created', models.CharField(max_length=75, blank=True)),
                ('object_image', models.ImageField(upload_to=b'', blank=True)),
                ('background_notes', models.TextField(blank=True)),
                ('slug', models.SlugField()),
                ('country_created', models.ForeignKey(to='notebook.Country')),
                ('giver', models.ForeignKey(related_name='giver', blank=True, to='notebook.Creator')),
                ('object_creator', models.ForeignKey(to='notebook.Creator')),
                ('receiver', models.ForeignKey(related_name='receiver', blank=True, to='notebook.Creator')),
            ],
        ),
    ]
