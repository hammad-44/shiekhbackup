# Generated by Django 4.2.2 on 2023-06-25 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toothpicks', '0008_alter_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='design',
        ),
    ]