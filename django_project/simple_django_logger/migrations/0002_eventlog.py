# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 18:26


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_django_logger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_level', models.IntegerField(choices=[(1, 'ERROR'), (2, 'DEBUG'), (3, 'WARN'), (4, 'INFO')], default=4)),
                ('message', models.TextField(blank=True)),
                ('stack_trace', models.TextField(blank=True)),
                ('tag', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Event Log',
                'verbose_name_plural': 'Event Logs',
            },
        ),
    ]
