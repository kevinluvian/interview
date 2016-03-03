# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviewer', '0002_auto_20160303_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('matric', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('department', models.ForeignKey(to='interviewer.InterviewDepartment')),
                ('group', models.ForeignKey(to='interviewer.InterviewGroup')),
            ],
        ),
    ]
