# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='my_register',
        ),
        migrations.RenameField(
            model_name='my_register',
            old_name='second_name',
            new_name='email',
        ),
    ]
