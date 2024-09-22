from django.urls import path
from dz_first_app import views

urlpatterns = [
    path('', views.hello, name='hello'),

]

