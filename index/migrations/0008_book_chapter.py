# Generated by Django 4.2 on 2023-04-10 14:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0007_alter_question_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=100)),
                ('ibsn', models.CharField(max_length=100)),
                ('rating', models.PositiveIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('active', models.BooleanField(default=True)),
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='chapter_id')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='description')),
                ('subject_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='chapter_id')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='index.book')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
