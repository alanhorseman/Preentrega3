# Generated by Django 5.0.4 on 2024-04-30 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_rename_cliente_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodosPagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('numero_tarjeta', models.PositiveIntegerField(unique=True)),
                ('cvv', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nacimiento', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='clientes',
        ),
        migrations.AddField(
            model_name='pais',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='pais_origen_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.pais'),
        ),
        migrations.AddField(
            model_name='metodospagos',
            name='titular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.usuarios'),
        ),
    ]
