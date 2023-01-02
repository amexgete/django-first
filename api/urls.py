from django.urls import path
from . import views

urlpatterns = [
	path('task-list/', views.tasklist.as_view()),

	path('task-delete/<int:pk>/', views.taskdel.as_view()),
]
