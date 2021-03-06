# Generated by Django 4.0 on 2021-12-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('paperweight', models.CharField(max_length=100)),
                ('sizes', models.CharField(max_length=100)),
                ('pages', models.IntegerField(default=3)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('ink', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('pagelayout', models.CharField(max_length=100)),
                ('creator', models.CharField(max_length=100)),
            ],
        ),
    ]
