# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ingredients", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="notes",
            field=models.TextField(blank=True, null=True),
        )
    ]
