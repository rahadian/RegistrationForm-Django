# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='time',
            field=models.DateField(default=datetime.datetime(2017, 4, 25, 8, 32, 24, 657548, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
