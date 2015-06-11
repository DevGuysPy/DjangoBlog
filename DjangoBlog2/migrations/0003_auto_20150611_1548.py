# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlog2', '0002_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_article',
            field=models.ForeignKey(to='DjangoBlog2.Article', null=True),
        ),
    ]
