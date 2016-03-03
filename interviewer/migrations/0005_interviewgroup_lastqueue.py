# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0004_auto_20160303_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewgroup',
            name='lastqueue',
            field=models.IntegerField(default=0),
        ),
    ]
