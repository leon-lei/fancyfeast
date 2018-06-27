# Generated by Django 2.0.6 on 2018-06-27 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tribes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='tribes.Tribe'),
        ),
    ]
