# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0003_auto_20160303_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
