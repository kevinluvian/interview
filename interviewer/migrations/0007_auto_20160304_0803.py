# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0006_interviewgroup_currentqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewdepartment',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='interviewgroup',
            name='code',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
