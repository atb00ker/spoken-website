# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0015_videotestimonial_admin_reviewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videotestimonial',
            name='location',
            field=models.CharField(max_length=2083),
        ),
    ]
