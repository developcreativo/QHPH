# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ciudades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('ciudad', models.ForeignKey(to='ciudades.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
