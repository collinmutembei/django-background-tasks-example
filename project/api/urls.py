from django.conf.urls import url
from django.http import JsonResponse

from . import views

urlpatterns = [
    url(r'^v1/tasks/$', views.tasks, name='tasks'),
]

