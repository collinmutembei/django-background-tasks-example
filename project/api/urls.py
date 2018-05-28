from django.urls import path
from django.http import JsonResponse

from . import views

urlpatterns = [
    path('v1/tasks/', views.tasks, name='tasks'),
]

# https://docs.djangoproject.com/en/2.0/releases/2.0/#simplified-url-routing-syntax
