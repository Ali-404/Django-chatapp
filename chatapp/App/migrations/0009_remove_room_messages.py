# Generated by Django 5.0.1 on 2024-02-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_room_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='messages',
        ),
    ]