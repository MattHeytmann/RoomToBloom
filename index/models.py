from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    description = models.TextField(verbose_name='description', null=True, blank=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")
    active = models.BooleanField(verbose_name="active", default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Class(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    parent_subject = models.ForeignKey('Subject', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name='description', null=True, blank=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")
    active = models.BooleanField(verbose_name="active", default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    
class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    parent_class = models.ForeignKey('Class', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(verbose_name='description', null=True, blank=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")
    active = models.BooleanField(verbose_name="active", default=True)
    test = models.BooleanField(verbose_name="active", default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    parent_note = models.ForeignKey('Note', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name="Question")
    answer = models.CharField(max_length=100, verbose_name="Answer")
    case_strict = models.BooleanField(verbose_name="is case strict", default=True)
    diacritic_strict = models.BooleanField(verbose_name="is diacritic strict", default=True)
    symbol_strict = models.BooleanField(verbose_name="is symbol strict", default=True)
    can_be_mashed = models.BooleanField(verbose_name="the result is in different order", default=True)
    active = models.BooleanField(verbose_name="active", default=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100,)
    sub_title = models.CharField(max_length=100,)
    ibsn = models.CharField(max_length=100,)
    rating = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])
    active = models.BooleanField(default=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Chapter(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    parent_book = models.ForeignKey('Book', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(verbose_name='description', null=True, blank=True)
    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="chapter_id")
    active = models.BooleanField(verbose_name="active", default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title