# Generated by Django 1.9.12 on 2017-02-16 09:46


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0035_publisheruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserunstate',
            name='owner_role_modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='coursestate',
            name='owner_role_modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalcourserunstate',
            name='owner_role_modified',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalcoursestate',
            name='owner_role_modified',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
