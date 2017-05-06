# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twote', '0003_user_should_ignore'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenspacesEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('start', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('creator', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'openchat_openspacesevent',
            },
        ),
        migrations.DeleteModel(
            name='RetweetEvent',
        ),
        migrations.RenameField(
            model_name='outgoingconfig',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='outgoingconfig',
            old_name='modified_date',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='outgoingtweet',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='outgoingtweet',
            old_name='modified_date',
            new_name='modified_at',
        ),
        migrations.RenameField(
            model_name='streamedtweet',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='streamedtweet',
            old_name='modified_date',
            new_name='modified_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favourites_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followers_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friends_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='user',
            name='location',
        ),
        migrations.RemoveField(
            model_name='user',
            name='protected',
        ),
        migrations.RemoveField(
            model_name='user',
            name='statuses_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='time_zone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='utc_offset',
        ),
        migrations.RemoveField(
            model_name='user',
            name='verified',
        ),
        migrations.AddField(
            model_name='outgoingtweet',
            name='original_tweet',
            field=models.CharField(default='fake tweet for default', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outgoingtweet',
            name='screen_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
