# Generated by Django 2.0.13 on 2019-05-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_auto_20190523_2113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CulculateFee',
        ),
        migrations.AlterField(
            model_name='submitattendance',
            name='date',
            field=models.DateField(verbose_name='打刻日'),
        ),
    ]
