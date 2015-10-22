# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0003_auto_20151021_1913'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='CartItem',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='order_by',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default=123456, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default='11322', to='ecommerce.Cart'),
            preserve_default=False,
        ),
    ]
