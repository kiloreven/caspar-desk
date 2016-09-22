# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 17:40
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('head', django.contrib.postgres.fields.jsonb.JSONField()),
                ('body', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('html', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TemplateField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hook_variable', models.CharField(max_length=128)),
                ('table_header', models.CharField(max_length=128)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caspar_desk.Table')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caspar_desk.Template')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caspar_desk.Template'),
        ),
    ]
