# Generated by Django 2.0.7 on 2018-07-17 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribes', '0006_auto_20180716_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='datetime',
        ),
    ]
