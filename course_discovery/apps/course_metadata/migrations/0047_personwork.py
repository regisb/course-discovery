# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-31 19:21


import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0046_courserun_reporting_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('value', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_works', to='course_metadata.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
