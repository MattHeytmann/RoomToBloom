# Generated by Django 4.2 on 2023-04-09 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0002_subject_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='chapter_id')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.subject')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
