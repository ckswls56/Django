from django.urls import path
from api.views import *

urlpatterns = [
    path('', apiOverview),
    path('task-list/',taskList, name='task-list'),
    path('task-detail/<str:pk>/',taskDetail, name='task-detail'),
    path('task-create/',taskCreate, name='task-create'),
    path('task-update/<str:pk>/',taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/',taskDelete, name='task-delete'),
    path('task-list-class/',TaskList.as_view(), name='task-list-class'),
    path('task-detail-class/<str:pk>/',TaskDetail.as_view(), name='task-detail-class'),
]
