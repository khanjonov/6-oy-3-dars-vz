# Generated by Django 5.1.4 on 2024-12-12 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Kurs nomi')),
                ('description', models.TextField(verbose_name='Kurs tavsifi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Talaba ismi')),
                ('email', models.EmailField(max_length=254, verbose_name='Talaba email')),
                ('enrolled_at', models.DateTimeField(auto_now_add=True, verbose_name="Ro'yxatdan o'tgan vaqt")),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.course', verbose_name='Kurs')),
            ],
        ),
    ]