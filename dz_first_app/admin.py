from django.contrib import admin
from .models import Task, SubTask, Category

# 2. Настройте отображение моделей в админке:
# для настройки отображения моделей Task, SubTask и Category.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'created_at')


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
