# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 18:48
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def add_after_subscribe_template(apps, schema_editor):
    EmailTemplate = apps.get_model('email', 'EmailTemplate')
    EmailTemplate.objects.create(mnemonic=settings.AFTER_SUBSCRIBE_TEMPLATE,
                                 subject='', html_content='', text_content='')


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_after_subscribe_template),
    ]
