# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0026_auto_20171002_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='page',
        ),
    ]