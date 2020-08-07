# Generated by Django 1.11.11 on 2018-07-09 21:26


import uuid

import django.db.models.deletion
import django_extensions.db.fields
import djchoices.choices
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0007_auto_20171004_1133'),
        ('course_metadata', '0084_auto_20180522_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(verbose_name='UUID')),
                ('title', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('sku', models.CharField(blank=True, max_length=128, null=True)),
                ('card_image_url', models.URLField(blank=True, null=True)),
                ('short_description', models.CharField(default=None, max_length=350)),
                ('full_description', models.TextField(blank=True, default=None, null=True)),
                ('access_length', models.IntegerField(default=365, help_text='number of days valid after purchase', null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('retired', 'Retired')], db_index=True, default='inactive', help_text='Used to determine whether journal is marketed or not.', max_length=24, validators=[djchoices.choices.ChoicesValidator({'active': 'Active', 'inactive': 'Inactive', 'retired': 'Retired'})])),
                ('slug', models.CharField(max_length=255)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Currency')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_metadata.Organization')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Partner')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='JournalBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='UUID')),
                ('title', models.CharField(help_text='The user-facing display title for this Journal Bundle', max_length=255, unique=True)),
                ('applicable_seat_types', models.ManyToManyField(blank=True, to='course_metadata.SeatType')),
                ('courses', models.ManyToManyField(blank=True, to='course_metadata.Course')),
                ('journals', models.ManyToManyField(blank=True, to='journal.Journal')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Partner')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]
