# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
            ],
            options={
                'ordering': ['-time'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='iAnimeModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=6)),
                ('key_word', models.CharField(max_length=80)),
                ('ori_type', models.CharField(max_length=20)),
                ('episode', models.IntegerField()),
                ('state', models.BooleanField(default=True)),
                ('img', models.ImageField(upload_to=b'Anime')),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ['-year'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='iBookModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=80)),
                ('publisher', models.CharField(max_length=80)),
                ('key_word', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=60)),
                ('state', models.BooleanField(default=True)),
                ('volume', models.IntegerField()),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to=b'Books')),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ['-year'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='iComicModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=60)),
                ('episode', models.IntegerField()),
                ('key_word', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=60)),
                ('state', models.BooleanField(default=True)),
                ('year', models.IntegerField()),
                ('img', models.ImageField(upload_to=b'Comic')),
                ('summary', models.TextField()),
            ],
            options={
                'ordering': ['-year'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['username'],
            },
            bases=(models.Model,),
        ),
    ]
