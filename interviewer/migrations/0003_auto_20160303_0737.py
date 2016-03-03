# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0002_auto_20160303_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewdepartment',
            name='status_desc',
            field=models.CharField(max_length=200),
        ),
    ]
