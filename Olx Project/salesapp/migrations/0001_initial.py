# Generated by Django 4.1.1 on 2022-09-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('kmrun', models.PositiveIntegerField()),
                ('place', models.CharField(max_length=120)),
            ],
        ),
    ]