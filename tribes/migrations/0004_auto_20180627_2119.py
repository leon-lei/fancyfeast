# Generated by Django 2.0.4 on 2018-06-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribes', '0003_auto_20180627_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='tribesmen',
            field=models.ManyToManyField(related_name='tribe', to='accounts.UserProfile'),
        ),
    ]
