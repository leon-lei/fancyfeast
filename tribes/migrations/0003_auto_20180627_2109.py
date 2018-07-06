# Generated by Django 2.0.4 on 2018-06-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('tribes', '0002_auto_20180626_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='event', to='accounts.UserProfile'),
        ),
    ]