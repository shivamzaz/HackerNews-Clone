# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_news_page'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_time', 'parent_comment__id']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['page', 'rank', '-created_time']},
        ),
    ]
