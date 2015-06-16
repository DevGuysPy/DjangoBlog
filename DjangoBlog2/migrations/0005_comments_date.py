# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlog2', '0004_auto_20150612_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 16, 13, 12, 32, 18000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
