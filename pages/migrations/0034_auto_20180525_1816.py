# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-05-25 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0033_auto_20180523_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtags',
            name='tag_image',
            field=models.ImageField(blank=True, null=True, upload_to='subtag_images/', verbose_name='Изображение тега'),
        ),
    ]
