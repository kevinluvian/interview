# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0006_interviewee_last_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewee',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
