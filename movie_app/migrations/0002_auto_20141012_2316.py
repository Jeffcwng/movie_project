# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie_name', models.CharField(max_length=50)),
                ('minute', models.IntegerField()),
                ('genre', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=30)),
                ('main_cast', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat_num', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['seat_num'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.CharField(max_length=50)),
                ('show_section', models.ForeignKey(related_name=b'show_time', to='movie_app.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cinema_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=20, blank=True)),
                ('zip_code', models.IntegerField(max_length=5, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paid', models.BooleanField(default=False)),
                ('for_movie', models.ForeignKey(related_name=b'seats', to='movie_app.Movie', null=True)),
                ('seat_ticket', models.ForeignKey(related_name=b'user_tickets', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='seat',
            name='show_num',
            field=models.ForeignKey(related_name=b'seat_number', to='movie_app.Showtime'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seat',
            name='user',
            field=models.ForeignKey(related_name=b'seats', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='cinema',
            field=models.ForeignKey(related_name=b'movie', to='movie_app.Theater'),
            preserve_default=True,
        ),
    ]
