# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0005_interviewgroup_lastqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewgroup',
            name='currentqueue',
            field=models.IntegerField(default=0),
        ),
    ]
