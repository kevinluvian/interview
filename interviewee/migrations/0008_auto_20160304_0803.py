# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0007_interviewee_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='score',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
