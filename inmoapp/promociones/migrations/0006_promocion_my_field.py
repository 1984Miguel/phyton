# Generated by Django 2.0.3 on 2018-03-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0005_auto_20180318_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='my_field',
            field=models.BooleanField(default=False),
        ),
    ]