# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-15 15:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brs_cmu', '0002_auto_20160412_1049'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bus_schedule',
            unique_together=set([('bus_schedule_id', 'bus_id')]),
        ),
    ]
