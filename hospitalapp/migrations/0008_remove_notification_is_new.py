# Generated by Django 5.0.6 on 2024-08-24 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0007_notification_is_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='is_new',
        ),
    ]
