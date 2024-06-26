# Generated by Django 5.0.6 on 2024-05-27 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la categoría', max_length=30)),
                ('descripcion_categoria', models.TextField(help_text='Descripción de la categoría')),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del proveedor de aviones', max_length=30)),
                ('contacto', models.TextField(help_text='Contacto del proveedor de aviones, puede ingresar el nombre del contacto telefono, email u otras redes sociales del mismo')),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'Otro')], max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del país', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del modelo de avión', max_length=30)),
                ('fabricante', models.ForeignKey(help_text='Fabricante del modelo de avión', on_delete=django.db.models.deletion.CASCADE, to='nyandu.fabricante')),
            ],
            options={
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(help_text='Matricula del avión', max_length=30)),
                ('capacidad', models.PositiveSmallIntegerField(help_text='Capacidad de pasajeros del avión')),
                ('autonomia', models.PositiveIntegerField(help_text='Autonomía del avión volando en línea recta a velocidad crucero, se expresa en millas')),
                ('modelo', models.ForeignKey(help_text='Fabricante del modelo de avión', on_delete=django.db.models.deletion.CASCADE, to='nyandu.modelo')),
            ],
            options={
                'verbose_name_plural': 'Aviones',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la provincia', max_length=30)),
                ('pais', models.ForeignKey(help_text='País al que pertenece la provincia', on_delete=django.db.models.deletion.CASCADE, to='nyandu.pais')),
            ],
            options={
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(help_text='Nombre y Apellido del empleado', max_length=60)),
                ('email', models.EmailField(help_text='Correo electrónico del empleado', max_length=254)),
                ('telefono', models.CharField(help_text='Teléfono del empleado', max_length=30)),
                ('direccion', models.CharField(help_text='Dirección donde reside el empleado', max_length=30)),
                ('localidad', models.CharField(help_text='Localidad donde reside el empleado', max_length=30)),
                ('categoria', models.ForeignKey(help_text='Categoria del empleado', on_delete=django.db.models.deletion.CASCADE, to='nyandu.categoria')),
                ('genero', models.ForeignKey(help_text='Género con el que se autopersive el empleado', on_delete=django.db.models.deletion.CASCADE, to='nyandu.genero')),
                ('provincia', models.ForeignKey(help_text='Provincia donde reside el empleado', on_delete=django.db.models.deletion.CASCADE, to='nyandu.provincia')),
            ],
            options={
                'verbose_name_plural': 'Empleados',
            },
        ),
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del aeropuerto', max_length=30)),
                ('codigo_iata', models.CharField(help_text='Código IATA del aeropuerto', max_length=3)),
                ('provincia', models.ForeignKey(help_text='Provincia donde está el aeropuerto', on_delete=django.db.models.deletion.CASCADE, to='nyandu.provincia')),
            ],
            options={
                'verbose_name_plural': 'Aeropuertos',
            },
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vuelo', models.DateField(blank=True, help_text='Día en que comienza el vuelo', null=True)),
                ('hora_vuelo', models.TimeField(blank=True, help_text='Hora en que despega el vuelo', null=True)),
                ('avion_vuelo', models.ForeignKey(help_text='Avión que realiza el vuelo', on_delete=django.db.models.deletion.CASCADE, to='nyandu.avion')),
                ('destino', models.ForeignKey(help_text='Aeropuerto donde llega el vuelo', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='nyandu.aeropuerto')),
                ('origen', models.ForeignKey(help_text='Aeropuerto donde sale el vuelo', on_delete=django.db.models.deletion.CASCADE, to='nyandu.aeropuerto')),
            ],
            options={
                'verbose_name_plural': 'Vuelos',
            },
        ),
    ]
