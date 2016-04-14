# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.CharField(max_length=48)),
                ('event_time', models.CharField(max_length=48)),
                ('event_type', models.CharField(max_length=48)),
                ('ordinal', models.CharField(max_length=48)),
                ('session_id', models.CharField(max_length=48)),
            ],
        ),
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.CharField(max_length=48)),
                ('area', models.CharField(max_length=48)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('meter_id', models.CharField(max_length=48)),
                ('street_address', models.CharField(max_length=48)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='meter_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Meter'),
        ),
    ]