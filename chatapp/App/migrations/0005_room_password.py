# Generated by Django 5.0.1 on 2024-02-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_message_created_at_room_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='password',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
