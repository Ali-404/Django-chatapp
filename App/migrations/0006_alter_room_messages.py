# Generated by Django 5.0.1 on 2024-02-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_room_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='messages',
            field=models.BinaryField(),
        ),
    ]