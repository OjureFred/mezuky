# Generated by Django 3.1.2 on 2020-10-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radioplay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plays',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='plays',
            name='plays',
        ),
        migrations.AddField(
            model_name='plays',
            name='channels',
            field=models.ManyToManyField(related_name='plays', to='radioplay.Channel'),
        ),
    ]
