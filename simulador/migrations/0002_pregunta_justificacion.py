# Generated by Django 4.1.3 on 2022-11-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='justificacion',
            field=models.TextField(default=''),
        ),
    ]