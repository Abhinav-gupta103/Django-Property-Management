# Generated by Django 4.0.3 on 2022-03-13 11:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('prop_image', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('property_type', models.CharField(choices=[('1', 'Flat'), ('2', 'Plot'), ('3', 'Villa'), ('4', 'Land'), ('5', 'Residential House'), ('6', 'Penthouse')], max_length=50)),
                ('status', models.CharField(max_length=35)),
                ('location', models.CharField(max_length=200, unique=True)),
                ('Owner', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Property_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.agent')),
                ('property', models.ForeignKey(default='ABC', on_delete=django.db.models.deletion.CASCADE, to='Home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d')),
                ('registration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 13, 17, 14, 16, 343465))),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.property')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.agent')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.owner')),
            ],
        ),
    ]
