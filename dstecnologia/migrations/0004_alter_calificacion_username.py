# Generated by Django 4.1.3 on 2022-11-26 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dstecnologia", "0003_calificacion_nivel_calificacion_seccion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calificacion",
            name="username",
            field=models.CharField(max_length=100),
        ),
    ]
