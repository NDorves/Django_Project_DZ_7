from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),

    ]
    title = models.CharField(max_length=100, unique=True)  # Название задачи.Уникально для даты.
    description = models.TextField(max_length=300, null=True, blank=True)  # Описание задачи.
    categories = models.ManyToManyField(Category)  # Категории задачи.Многие ко многим.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='New')  # Статус задачи.Выбор из:New,In progress,Pending,Blocked,Done
    deadline = models.DateTimeField()  # Дата и время дедлайн.
    created_at = models.DateTimeField(auto_now_add=True)  #: Дата/время создания.Авт-тич-е зап-е.

    def __str__(self):
        return self.title


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'),

    ]
    title = models.CharField(max_length=100)                #Название подзадачи.
    description = models.TextField()                        # Описание  подзадачи.
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)  # Категории задачи.Многие ко многим.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='New')                # Статус задачи.Выбор из:New,In progress,Pending,Blocked,Done
    deadline = models.DateTimeField()                       # Дата/время дедлайн.
    created_at = models.DateTimeField(auto_now_add=True)    #: Дата/время создания.Авт-тич-е зап-е.

    def __str__(self):
        return self.title
