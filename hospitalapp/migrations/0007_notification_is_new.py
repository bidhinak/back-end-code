# Generated by Django 5.0.6 on 2024-08-24 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0006_doctoradd_mobile_doctoradd_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_new',
            field=models.BooleanField(default=True),
        ),
    ]
