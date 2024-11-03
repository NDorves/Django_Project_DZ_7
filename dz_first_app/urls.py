# Добавьте маршруты в файле urls.py, чтобы использовать эти классы.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from dz_first_app import views
from dz_first_app.views import *


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', views.hello, name='hello'),
    path('', include(router.urls)),
    path('user=tasks/', UserTaskListView.as_view()),
    path('user-subtasks/', UserSubTaskListView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view(), name='login_refresh'),
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


