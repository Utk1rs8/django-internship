# Generated by Django 5.1.1 on 2024-10-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_bikes_delete_bike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=25)),
                ('confirmpassword', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]