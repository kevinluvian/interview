# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewee',
            name='matric',
            field=models.CharField(max_length=200),
        ),
    ]
