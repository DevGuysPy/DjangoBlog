# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('article_text', models.TextField()),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('article_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'articles',
            },
        ),
    ]
