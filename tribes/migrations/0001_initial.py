# Generated by Django 2.0.6 on 2018-08-22 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=80)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('datetime', models.DateTimeField()),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=2)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('yes', models.IntegerField(default=0)),
                ('no', models.IntegerField(default=0)),
                ('attendees', models.ManyToManyField(related_name='event', to='accounts.UserProfile')),
            ],
            options={
                'ordering': ('datetime',),
            },
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='tribe_image')),
                ('chieftain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chieftain', to='accounts.UserProfile')),
                ('tribesmen', models.ManyToManyField(related_name='tribe', to='accounts.UserProfile')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='tribe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='tribes.Tribe'),
        ),
    ]
