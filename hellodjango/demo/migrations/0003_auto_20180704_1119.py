# Generated by Django 2.0.6 on 2018-07-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20180704_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='bad_count',
            field=models.IntegerField(db_column='tbcount', default=0, verbose_name='差评数'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='good_count',
            field=models.IntegerField(db_column='tgcount', default=0, verbose_name='好评数'),
        ),
    ]
