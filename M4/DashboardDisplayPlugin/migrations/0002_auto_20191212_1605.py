# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-12 21:05
from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    DashboardDisplayPlugin = apps.get_model("DashboardDisplayPlugin", "DashboardDisplayPlugin")
    DisplayPlugin = apps.get_model('System', 'DisplayPlugin')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    FrontEnd = apps.get_model('System', 'FrontEnd')
    Plugin = apps.get_model('djangoplugins', 'Plugin')

    db_alias = schema_editor.connection.alias
    DashboardDisplayPlugin.objects.using(db_alias).create(pk=1, name='default-widgets', title="Default Widgets",
                                                          logo='img/m4.png',
                                                          slogan='M4 is for Modern Monitoring and Management',
                                                          template='default/default')
    DisplayPlugin.objects.using(db_alias).create(id=1, name='(DashboardDisplayPlugin) Default Widgets', object_id=1,
                                                 content_type=ContentType.objects.get(pk=23))
    FrontEnd.objects.using(db_alias).create(pk=1, name='dashboard', title='Default Dashboard',
                                            plugin=Plugin.objects.get(name='dashboard'))


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    DashboardDisplayPlugin = apps.get_model("DashboardDisplayPlugin", "DashboardDisplayPlugin")
    DisplayPlugin = apps.get_model('System', 'DisplayPlugin')
    FrontEnd = apps.get_model('System', 'FrontEnd')
    db_alias = schema_editor.connection.alias
    DashboardDisplayPlugin.objects.using(db_alias).get(pk=1).delete()
    DisplayPlugin.objects.using(db_alias).get(id=1).delete()
    FrontEnd.objects.using(db_alias).get(pk=1).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('DashboardDisplayPlugin', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]