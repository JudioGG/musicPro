# Generated by Django 3.1.3 on 2021-05-25 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210525_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria_prod',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='tipo_prod',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Tipo_producto',
        ),
    ]
