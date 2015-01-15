# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0004_auto_20150114_0618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
