# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 09:32
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('greeting', models.TextField(blank=True, null=True)),
                ('number', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('number', models.CharField(max_length=20)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('token', models.IntegerField(default=core.models.generate_token)),
            ],
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='core.Queue'),
        ),
        migrations.AlterUniqueTogether(
            name='patient',
            unique_together=set([('time', 'token')]),
        ),
    ]