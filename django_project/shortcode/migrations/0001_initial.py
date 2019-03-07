# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shortcode.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLDefine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=250, validators=[shortcode.validators.is_url_valid])),
                ('shortened_url', models.CharField(unique=True, max_length=8, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'URL Entry',
                'verbose_name_plural': 'URL Entries',
            },
        ),
    ]
