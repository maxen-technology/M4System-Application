# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-12 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SSHSourcePlugin', '0002_auto_20191212_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshsourceplugin',
            name='content',
            field=models.CharField(default='echo 1',
                                   help_text='Put the script content here.  It will be executed by the shell you select.',
                                   max_length=4096, verbose_name='The Script'),
        ),
        migrations.AlterField(
            model_name='sshsourceplugin',
            name='shell',
            field=models.CharField(default='/bin/bash', help_text='This is usually /bin/bash on linux.', max_length=256,
                                   verbose_name='Remote Shell'),
        ),
    ]
