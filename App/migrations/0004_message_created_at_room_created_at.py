# Generated by Django 5.0.1 on 2024-02-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]