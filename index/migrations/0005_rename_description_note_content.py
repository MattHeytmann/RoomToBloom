# Generated by Django 4.2 on 2023-04-10 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='description',
            new_name='content',
        ),
    ]
