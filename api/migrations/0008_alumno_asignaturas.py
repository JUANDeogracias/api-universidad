# Generated by Django 5.1.3 on 2024-11-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_profesor_remove_alumno_fecha_registro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='asignaturas',
            field=models.ManyToManyField(blank=True, related_name='alumnos', to='api.asignatura'),
        ),
    ]
