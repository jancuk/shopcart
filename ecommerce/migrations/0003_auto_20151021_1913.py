# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_auto_20151021_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='products',
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='ecommerce.Order'),
        ),
        migrations.DeleteModel(
            name='Merchant',
        ),
    ]
