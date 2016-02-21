# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cities', models.IntegerField(verbose_name=b'NumCities')),
                ('users', models.IntegerField(verbose_name=b'Users')),
                ('ts', models.DateTimeField(auto_now_add=True, verbose_name=b'ts')),
            ],
        ),
    ]
