# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-12 22:39
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Setting = apps.get_model("System", "Setting")
    db_alias = schema_editor.connection.alias
    Setting.objects.using(db_alias).create(key='frontend_default', value='dashboard')


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Setting = apps.get_model("System", "Setting")
    db_alias = schema_editor.connection.alias
    Setting.objects.using(db_alias).get(key='frontend_default').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('System', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

