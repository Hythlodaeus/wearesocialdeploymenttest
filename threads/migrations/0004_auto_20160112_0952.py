# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0003_auto_20160111_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 12, 9, 52, 16, 816930, tzinfo=utc)),
        ),
    ]
