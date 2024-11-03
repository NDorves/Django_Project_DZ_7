from django.contrib.auth.models import PermissionsMixin, UserManager, User
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

# #class User(models.Model):
# class User(AbstractBaseUser):
#
#     username = models.CharField(_("username"), max_length=50, unique=True,
#                                 error_messages={"unique": _("A user with that username already exists."), })
#     first_name = models.CharField(_("first name"), max_length=40, validators=[MinLengthValidator(2)],)
#     last_name = models.CharField(_("last name"), max_length=40, validators=[MinLengthValidator(2)],)
#     email = models.EmailField(_("email address"), max_length=150, unique=True)
#     phone = models.CharField(max_length=75, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(name="registered", auto_now_add=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     deleted = models.BooleanField(default=False)
#
#     # USERNAME_FIELD = "email"
#     # REQUIRED_FIELDS = ["username", "first_name", "last_name",]
#     #
#     # objects = UserManager()
#
#     def __list__(self):
#         return f"{self.last_name} {self.first_name}"


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True) #включениe поля owner

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks', null=True)

    def __str__(self):  # Добавить метод str, который возвращает название подзадачи.
        return self.title

    #
    class Meta:  # Добавить класс Meta с настройками
        db_table = 'task_manager_subtask'  # Имя таблицы в базе данных: 'task_manager_subtask'.
        ordering = ['-created_at']  # Сортировка по убыванию даты создания.
        verbose_name = 'SubTask'  # Человекочитаемое имя модели: 'SubTask'.
        unique_together = ['title']  # Уникальность по полю 'title'.


