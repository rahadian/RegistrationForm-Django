# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
