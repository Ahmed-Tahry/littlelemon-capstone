# Generated by Django 5.0 on 2023-12-26 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='price',
        ),
    ]
