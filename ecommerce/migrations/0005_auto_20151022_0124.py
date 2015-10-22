# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0004_auto_20151021_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='customer',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=False,
        ),
    ]
