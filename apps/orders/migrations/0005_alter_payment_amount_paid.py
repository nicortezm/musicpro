# Generated by Django 3.2.3 on 2021-05-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210525_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(verbose_name='monto pagado'),
        ),
    ]
