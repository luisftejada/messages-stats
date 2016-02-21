# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=64, verbose_name=b'State')),
                ('city', models.CharField(max_length=64, verbose_name=b'City')),
                ('username', models.CharField(max_length=64, verbose_name=b'User')),
                ('message', models.TextField(verbose_name=b'Message')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'Date')),
            ],
            options={
                'ordering': ['state', 'city', 'create_time'],
            },
        ),
    ]
