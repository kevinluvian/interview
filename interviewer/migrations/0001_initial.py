# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewDepartment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('status', models.IntegerField(default=0)),
                ('status_desc', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='interviewdepartment',
            name='group',
            field=models.ForeignKey(to='interviewer.InterviewGroup'),
        ),
    ]
