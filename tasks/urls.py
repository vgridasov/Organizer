from django.urls import path
from . import views

urlpatterns = [
    path('task/<int:task_id>/', views.task_detail, name='task'),
    path('about', views.about, name='about'),
    path('', views.home, name='home'),
]
