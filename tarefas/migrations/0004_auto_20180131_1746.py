# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-01-31 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_auto_20180131_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
    ]
