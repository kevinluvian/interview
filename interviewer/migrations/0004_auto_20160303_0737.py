# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0003_auto_20160303_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewdepartment',
            name='status_desc',
            field=models.IntegerField(default=0),
        ),
    ]
