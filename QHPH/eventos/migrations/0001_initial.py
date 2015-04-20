# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
