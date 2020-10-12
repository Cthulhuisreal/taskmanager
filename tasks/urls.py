from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

# API эндпоинты
urlpatterns = format_suffix_patterns([
    path('', views.MyTaskList.as_view(), name='mytask-list'),
])
