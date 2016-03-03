# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0004_auto_20160303_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewee',
            name='queuenum',
            field=models.IntegerField(default=0),
        ),
    ]
