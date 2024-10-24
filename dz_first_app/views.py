
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
#from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.reverse import reverse
from dz_first_app.models import SubTask, Task, Category
from dz_first_app.serializers.api_task import SubTaskCreateSerializer, TaskSerializer, TaskListCreateSerializers, \
    SubTaskSerializer, CategorySerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.utils import timezone
from django.db.models import Count
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def hello(request):
    return HttpResponse("Hello, NDorves")


class TaskStatisticsView(APIView):
    def get(self, request):
        total_tasks = Task.objects.count()
        tasks_by_status = Task.objects.values('status').annotate(count=Count('id'))  # Убедитесь, что используете Count
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        statistics = {
            "total_tasks": total_tasks,
            "tasks_by_status": {item['status']: item['count'] for item in tasks_by_status},
            "overdue_tasks": overdue_tasks,
        }

        return Response(statistics, status=status.HTTP_200_OK)


class TaskPagination(PageNumberPagination): #Кастомный класс пагинации, наследуемый от PageNumberPagination
    page_size = 5   # Определяет количество элементов на странице
    page_size_query_param = 'page_size'  #Позволяет клиентам указывать размер страницы через параметр запроса page_size.
    max_page_size = 100     # Ограничивает максимальный размер страницы

# class TaskCursorPagination(CursorPagination):
#     page_size = 5
#     ordering = 'created_at'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = TaskPagination

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = category.tasks.count()
        return Response({'task_count': task_count})


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    # pagination_class = TaskCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return TaskListCreateSerializers
    #     return TaskSerializer
    #
    # def get(self, request, *args, **kwargs):
    #     tasks = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(tasks)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(tasks, many=True)
    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class()(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# class SubTaskCursorPagination(CursorPagination):
#     page_size = 5
#     ordering = 'created_at'


class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    pagination_class = SubTaskPagination

#    pagination_class = SubTaskCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return SubTaskCreateSerializer
    #     return SubTaskSerializer

    # def get(self, request, *args, **kwargs):
    #     subtasks = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(subtasks)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(subtasks, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class()(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #


class SubTaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer










