# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0002_remove_registration_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateField()),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_contents', models.TextField(max_length=100)),
                ('user_id', models.ForeignKey(to='auths.Registration')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='registration',
            name='mobile',
            field=models.IntegerField(max_length=10),
            preserve_default=True,
        ),
    ]
