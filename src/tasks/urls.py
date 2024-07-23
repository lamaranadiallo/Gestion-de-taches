from django.urls import path
from tasks import views

urlpatterns = [
    path('',views.task_list,name='task_list'),
    path('task/<int:pk>/', views.task_detail,name='task_detail'),
    path('task/new/',views.task_create,name='task_create'),
    path('task/<int:pk>/edit/',views.task_update,name='task_update'),
    path('task/<int:pk>/delete/',views.task_delete,name='task_delete'),
]