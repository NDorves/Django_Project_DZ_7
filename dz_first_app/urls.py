# Добавьте маршруты в файле urls.py, чтобы использовать эти классы.
#import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from dz_first_app import views
from dz_first_app.views import *


# router = DefaultRouter()
# router.register(r'tasks', TaskListCreateViewSet)
urlpatterns = [
    path('', views.hello, name='hello'),
 #    path('task_create/', task_create),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task_statistics'),
 # #   path('view/', simple_view),
 #    path('task_list/', task_list),
 #    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
 #    path('subtasks/<int:pk>', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_detail_update_delete'),
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
#    path('tasks/<str:title>/', TaskDetailUpdateDeleteView.as_view(), name='task_update_delete'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task_update_delete'),
    path('sub/tasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
    path('sub/tasks/<int:pk>', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_update_delete')
]

