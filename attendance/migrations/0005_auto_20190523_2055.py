# Generated by Django 2.0.13 on 2019-05-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20190523_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitattendance',
            name='place',
            field=models.CharField(choices=[(1, 'TANKS'), (2, 'Red Tails'), (3, 'ANNIE HALL'), (4, 'NOKUROXY'), (5, '七'), (6, 'ART MON ZEN')], default=None, max_length=50, verbose_name='出勤場所名'),
        ),
    ]
