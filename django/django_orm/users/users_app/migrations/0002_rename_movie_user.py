# Generated by Django 4.2.4 on 2023-08-15 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='User',
        ),
    ]