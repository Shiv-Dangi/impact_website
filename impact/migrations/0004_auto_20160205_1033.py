# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impact', '0003_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='subject',
            new_name='lname',
        ),
    ]
