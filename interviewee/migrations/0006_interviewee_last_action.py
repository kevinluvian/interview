# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0005_interviewee_queuenum'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewee',
            name='last_action',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
