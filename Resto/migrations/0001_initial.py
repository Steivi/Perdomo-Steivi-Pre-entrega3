# Generated by Django 4.1.6 on 2023-02-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('DNI', models.IntegerField()),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('DNI_cliente', models.IntegerField()),
                ('numero_mesa', models.ImageField(upload_to='')),
                ('num_invitados', models.IntegerField()),
                ('fecha_de_reservacion', models.DateTimeField()),
            ],
        ),
    ]
