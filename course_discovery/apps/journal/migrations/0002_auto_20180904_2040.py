# Generated by Django 1.11.15 on 2018-09-04 20:40


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='slug',
        ),
        migrations.AddField(
            model_name='journal',
            name='about_page_id',
            field=models.IntegerField(default=0),
        ),
    ]
