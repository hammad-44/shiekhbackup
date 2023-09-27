# Generated by Django 4.2.2 on 2023-06-25 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toothpicks', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('product', models.CharField(max_length=55)),
                ('quantity', models.CharField(max_length=55)),
                ('message', models.TextField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('design', models.BooleanField(default=False)),
            ],
        ),
    ]