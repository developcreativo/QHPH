# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_evento_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='hora',
            field=models.DateTimeField(blank=True),
        ),
    ]
