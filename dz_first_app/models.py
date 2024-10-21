from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  # Добавить метод str, который возвращает название категории.
        return self.name

    class Meta:  # Добавить класс Meta с настройками:
        db_table = 'task_manager_category'  # Имя таблицы в базе данных: 'task_manager_category'.
        verbose_name = 'Category'  # Человекочитаемое имя модели: 'Category'.
        unique_together = ['name']  # Уникальность по полю 'name'.


class Task(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'), ]

    title = models.CharField(max_length=100, unique=True)  # Название задачи.Уникально для даты.
    description = models.TextField(max_length=300, null=True, blank=True)  # Описание задачи.
    categories = models.ManyToManyField(Category, blank=True)  # Категории задачи.Многие ко многим.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='New')  # Статус задачи.Выбор из:New,In progress,Pending,Blocked,Done
    deadline = models.DateTimeField(default='Now')  # Дата и время дедлайн.
    created_at = models.DateTimeField(auto_now_add=True)  #: Дата/время создания.Авт-тич-е зап-е.
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'task_manager_task'  # Имя таблицы в базе данных: 'task_manager_task'.
        ordering = ['-created_at', 'status', 'deadline']  # Сортировка по убыванию даты создания.
        verbose_name = 'Task'  # Человекочитаемое имя модели: 'Task'.
        unique_together = ['title']  # Уникальность по полю 'title'.


class SubTask(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done'), ]  # Выбор из:New,In progress,Pending,Blocked,Done

    title = models.CharField(max_length=100)  # Название подзадачи.
    description = models.TextField()  # Описание  подзадачи.
    task = models.ForeignKey(Task, related_name='subtasks',
                             on_delete=models.CASCADE)  # Категории задачи.Многие ко многим.
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default='New')  # Статус задачи.Выбор из:New,In progress,Pending,Blocked,Done
    deadline = models.DateTimeField()  # Дата/время дедлайн(срок).
    created_at = models.DateTimeField(auto_now_add=True)  #: Дата/время создания.Авт-тич-е зап-е.
    is_banned = models.BooleanField(default=False)

    def __str__(self):  # Добавить метод str, который возвращает название подзадачи.
        return self.title

    #
    class Meta:  # Добавить класс Meta с настройками
        db_table = 'task_manager_subtask'  # Имя таблицы в базе данных: 'task_manager_subtask'.
        ordering = ['-created_at']  # Сортировка по убыванию даты создания.
        verbose_name = 'SubTask'  # Человекочитаемое имя модели: 'SubTask'.
        unique_together = ['title']  # Уникальность по полю 'title'.
