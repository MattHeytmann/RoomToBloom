from django.contrib import admin
from .models import Subject, Class, Note, Question


@admin.action(description='make active')
def make_active(modeladmin, request, queryset):
    queryset.update(active=True)


@admin.action(description='make unactive')
def make_unactive(modeladmin, request, queryset):
    queryset.update(active=False)


@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "description")
    actions = [make_active, make_unactive]

@admin.register(Class)
class Subject(admin.ModelAdmin):
    list_display = ("title", "parent_subject", "author")
    search_fields = ("title", "parent_subject", "description")
    actions = [make_active, make_unactive]

@admin.register(Note)
class Note(admin.ModelAdmin):
    list_display = ("title", "parent_class", "author", "created_at")
    search_fields = ("title", "parent_class", "description", "created_at")
    actions = [make_active, make_unactive]

@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title", "parent_note", "answer")
    actions = [make_active, make_unactive]


admin.site.site_header = "Room to Bloom admin"
