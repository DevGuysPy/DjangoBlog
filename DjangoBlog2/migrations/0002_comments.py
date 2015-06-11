# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBlog2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('comment_text', models.TextField()),
                ('comment_article', models.ForeignKey(to='DjangoBlog2.Article')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
