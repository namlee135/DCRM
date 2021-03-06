# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEIPDCRM', '0008_auto_20170326_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='copyright_name',
            field=models.CharField(help_text='Corpyright name is displayed on the footer of the page, leave a blank will display the source name.', max_length=255, null=True, verbose_name='Copyright Name'),
        ),
        migrations.AddField(
            model_name='setting',
            name='copyright_year',
            field=models.FloatField(help_text='If input 2016, the final display is \xa9 2010-1490499101, leave a blank will display \xa9 %d', max_length=255, null=True, verbose_name='Starting Year of Copyright'),
        ),
        migrations.AddField(
            model_name='setting',
            name='footer_icp',
            field=models.CharField(help_text='ICP Number is displayed on the footer of the page.', max_length=255, null=True, verbose_name='ICP Number'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='qq_group_url',
            field=models.URLField(help_text='Show QQ Group link in mobile package info page.', max_length=255, null=True, verbose_name='QQ Group URL'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='weibo_url',
            field=models.URLField(help_text='Show Weibo link in mobile package info page.', max_length=255, null=True, verbose_name='Weibo URL'),
        ),
    ]
