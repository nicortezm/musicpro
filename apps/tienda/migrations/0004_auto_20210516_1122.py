# Generated by Django 3.2.3 on 2021-05-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20210513_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha creación'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha modificación'),
        ),
    ]
