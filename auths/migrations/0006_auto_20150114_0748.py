# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0005_auto_20150114_0649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]
