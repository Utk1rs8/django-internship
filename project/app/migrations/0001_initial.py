# Generated by Django 3.2.25 on 2024-09-21 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('engine_capacity', models.TextField(max_length=150)),
                ('malage', models.TextField(max_length=150)),
                ('transmission', models.TextField(max_length=150)),
                ('weight', models.TextField(max_length=150)),
                ('fuel_tank', models.TextField(max_length=150)),
                ('power', models.TextField(max_length=150)),
                ('tourque', models.TextField(max_length=150)),
            ],
        ),
    ]