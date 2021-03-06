# Generated by Django 2.0.3 on 2018-03-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('Url', models.URLField()),
                ('descripcion', models.TextField()),
                ('tipo', models.CharField(choices=[('VEN', 'Promociones en venta'), ('PRO', 'Promociones próximas'), ('ENT', 'Promociones entregadas')], max_length=3)),
            ],
        ),
    ]
