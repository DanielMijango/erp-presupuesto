# Generated by Django 5.0.6 on 2024-06-01 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presupuesto', '0002_remove_presupuesto_gastos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presupuesto',
            name='solicitud_presupuesto',
        ),
    ]
