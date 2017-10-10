# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-08 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('myapp', '0002_articlepluginmodel_associateditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myapp_childplugin', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ParentPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='myapp_parentplugin', serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
