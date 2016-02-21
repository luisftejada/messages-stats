# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='stat_id',
            field=models.CharField(default='1', max_length=1, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
