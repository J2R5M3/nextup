# Generated by Django 3.2 on 2021-04-15 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nextup_api', '0006_auto_20210414_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='last_showed',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
