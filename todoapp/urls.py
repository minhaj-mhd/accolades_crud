from django.urls import path
from .views import TodoAPIView,TodoDetailAPIView

urlpatterns = [
    
    path('todos/',TodoAPIView.as_view(),name='todo-get-list'),
    path('todos/<int:pk>/',TodoDetailAPIView.as_view(),name="todo-detail")
]
