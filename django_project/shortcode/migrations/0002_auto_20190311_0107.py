# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shortcode.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortcode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldefine',
            name='url',
            field=models.CharField(max_length=5000, validators=[shortcode.validators.is_url_valid]),
        ),
    ]
