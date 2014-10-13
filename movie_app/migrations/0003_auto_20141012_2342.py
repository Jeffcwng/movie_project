# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_auto_20141012_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_num',
            field=models.CharField(max_length=3),
        ),
    ]
