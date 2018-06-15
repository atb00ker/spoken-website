# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0014_auto_20180613_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotestimonial',
            name='admin_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
