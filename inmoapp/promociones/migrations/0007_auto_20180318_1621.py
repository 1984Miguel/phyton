# Generated by Django 2.0.3 on 2018-03-18 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0006_promocion_my_field'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocion',
            old_name='my_field',
            new_name='banner',
        ),
    ]
