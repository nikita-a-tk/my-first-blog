# Generated by Django 2.2 on 2019-04-28 19:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190428_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 28, 19, 23, 5, 831022, tzinfo=utc)),
        ),
    ]
