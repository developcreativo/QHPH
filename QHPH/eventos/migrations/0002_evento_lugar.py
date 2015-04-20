# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='lugar',
            field=models.ForeignKey(default=1, to='lugares.Lugar'),
            preserve_default=False,
        ),
    ]
