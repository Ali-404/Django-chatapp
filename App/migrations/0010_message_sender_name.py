# Generated by Django 5.0.1 on 2024-02-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_remove_room_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender_name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
