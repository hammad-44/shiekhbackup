# Generated by Django 4.2.2 on 2023-06-24 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toothpicks', '0004_alter_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
        ),
    ]
