# Generated by Django 4.2.2 on 2023-08-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_sensorshampoo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
