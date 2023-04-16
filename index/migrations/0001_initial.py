# Generated by Django 4.2 on 2023-04-09 13:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='chapter_id')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
