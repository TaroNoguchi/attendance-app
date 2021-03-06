# Generated by Django 2.0.13 on 2019-05-23 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20190523_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='CulculateFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='submitattendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 5, 23, 11, 29, 36, 993617, tzinfo=utc), verbose_name='打刻日'),
        ),
        migrations.AlterField(
            model_name='submitattendance',
            name='time',
            field=models.TimeField(verbose_name='打刻時間'),
        ),
    ]
