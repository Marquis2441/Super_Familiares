# Generated by Django 4.1.1 on 2022-09-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperFamiliares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
                ('peso_kg', models.IntegerField()),
            ],
        ),
    ]
