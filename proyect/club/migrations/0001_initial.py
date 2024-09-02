# Generated by Django 5.1 on 2024-09-01 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instalacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('capacidad', models.IntegerField()),
                ('necesita_reserva', models.BooleanField(default=False)),
                ('horario_disponible', models.CharField(blank=True, max_length=100, null=True)),
                ('disponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cuota_mensual', models.DecimalField(blank=True, decimal_places=2, help_text='Cuota mensual para participar en este deporte.', max_digits=8, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('instalaciones', models.ManyToManyField(related_name='deportes', to='club.instalacion')),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('año_nacimiento', models.IntegerField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('activo', models.BooleanField(default=True)),
                ('deportes', models.ManyToManyField(related_name='socios', to='club.deporte')),
            ],
        ),
    ]
