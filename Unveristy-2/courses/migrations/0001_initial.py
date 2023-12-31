# Generated by Django 3.2.9 on 2021-11-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=512)),
                ('start_data', models.DateField(blank=True, null=True)),
                ('is_activate', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120, null=True)),
                ('degree', models.CharField(choices=[('kollage', 'kollage'), ('unversity', 'unversity'), ('magister', 'magister')], max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('specialities', models.ManyToManyField(to='courses.Speciality')),
                ('teachers', models.ManyToManyField(to='courses.Teacher')),
            ],
        ),
    ]
