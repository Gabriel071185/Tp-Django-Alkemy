# Generated by Django 4.2 on 2024-03-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0003_alter_proveedor_cuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre del proveedor '),
        ),
    ]
