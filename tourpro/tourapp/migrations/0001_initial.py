# Generated by Django 5.0.2 on 2024-02-26 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_Name', models.CharField(max_length=120, verbose_name='hotel name')),
                ('H_Locaation', models.CharField(max_length=120, verbose_name='hotel addres')),
                ('Discreption', models.TextField(max_length=200)),
                ('Payment', models.CharField(max_length=120)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourapp.reat')),
            ],
        ),
    ]
