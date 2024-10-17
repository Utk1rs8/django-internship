# Generated by Django 3.2.25 on 2024-10-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_register_delete_registers'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessoriesItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='image/')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
