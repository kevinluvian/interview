# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewdepartment',
            name='last_action',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='interviewdepartment',
            name='description',
            field=models.TextField(),
        ),
    ]
