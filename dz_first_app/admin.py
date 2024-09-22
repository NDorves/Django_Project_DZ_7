from django.contrib import admin
from .models import Task, SubTask, Category

# Register your models here.
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Category)


# 2. Настройте отображение моделей в админке:
# В файле admin.py вашего приложения добавьте классы администратора
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
