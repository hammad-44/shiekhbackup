# Generated by Django 4.2.2 on 2023-06-25 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toothpicks', '0007_alter_order_design'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='number',
            field=models.CharField(max_length=255),
        ),
    ]