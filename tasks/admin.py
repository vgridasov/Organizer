from django.contrib import admin
from .models import *


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_create', 'task_name', 'task_from', 'task_description', 'task_status', 'task_assign_user')
    list_display_links = ('id', 'task_name')
    search_fields = ('task_name', 'task_description')
    list_filter = ('task_status', 'time_create')


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'patronymic',
        'fio',
        'company',
        'department',
        'position',
        'location',
        'phone',
        'email',
        'slug'
    )
    list_display_links = (
        'user',
        'fio'
    )


admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Profile, ProfileAdmin)
