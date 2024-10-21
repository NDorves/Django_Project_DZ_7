# --------------------Задание 1:Определите SubTaskCreateSerializer в файле serializers --> (api_task.py)-----------
import datetime
from rest_framework import serializers
from dz_first_app.models import Task, SubTask, Category


# Переопределите поле created_at как read_only.


class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)  # поле created_at доступно только для чтения (read_only).

    class Meta:
        model = SubTask
        fields = '__all__'


# ----------------Задание 2:Определите CategoryCreateSerializer в файле serializers.py.--------------------
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    # Переопределите метод create для проверки уникальности названия категории.

    def create(self, validated_data):
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError('Category mit diese Name bereits  existiert schon')
        return super().create(validated_data)

    #  Переопределите метод update для аналогичной проверки при обновлении.
    def update(self, instance, validated_data):
        if 'name' in validated_data and Category.objects.filter(name=validated_data['name']).exclude(
                id=instance.id).exists():
            raise serializers.ValidationError('Category mit diese Name bereits  existiert schon')
        return super().update(instance, validated_data)


# --------------------Задание 3:Определите TaskDetailSerializer в файле serializers.py.---------------------
# Вложите SubTaskSerializer внутрь TaskDetailSerializer.
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtask = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    # @classmethod
    # def as_view(cls):
    #     pass


# -----------------------Задание 4: Определите TaskCreateSerializer в файле serializers.py.--------------------

class TaskListCreateSerializers(serializers.ModelSerializer):  # эндпойнт для создания новой задачи.

    class Meta:
        model = Task
        fields = '__all__'

    # Переопределите метод validate_deadline для проверки даты.
    def validate_deadline(self, value):
        value = datetime.datetime.now()
        if value < datetime.datetime.now():
            raise serializers.ValidationError('Datum kann nicht in Vergangenheit sein.')
        return value

# # ----------------------------HAFG 11--------------------------
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'
#         # ordering = ['status', 'deadline']
#         # get_latest_by = 'deadline'
#
#
# dataDZ = {
#     "title": "HAFG 11 dubl1. Pruefen",
#     "description": "Das functioniert",
#     "status": "In progress",
#     "deadline": "2024-10-07T12:00:00Z"
#
# }
#
# serializer = TaskSerializer(data=dataDZ)
#
# # Проверка валидности данных
# if serializer.is_valid():
#     # Сохранение задачи в базе данных
#     task = serializer.save()
#     print('Good data:', serializer.validated_data)
# else:
#     # Печать ошибок, если данные не валидны
#     print('Invalid data:', serializer.errors)
