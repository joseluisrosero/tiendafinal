# Generated by Django 5.1.1 on 2024-10-20 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0005_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
