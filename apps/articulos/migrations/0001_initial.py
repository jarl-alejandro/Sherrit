# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140)),
                ('contenido', models.TextField(default=b'')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('votos', models.IntegerField(default=0)),
                ('slug', models.SlugField(editable=False)),
                ('creador', models.ForeignKey(to='usuarios.Perfil')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
