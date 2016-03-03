# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0002_auto_20160303_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
