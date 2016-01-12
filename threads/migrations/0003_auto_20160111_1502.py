# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0002_auto_20160111_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 11, 15, 2, 6, 593154, tzinfo=utc)),
        ),
    ]
