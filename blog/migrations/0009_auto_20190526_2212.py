# Generated by Django 2.2 on 2019-05-26 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190526_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 19, 12, 16, 800865, tzinfo=utc)),
        ),
    ]
