from rest_framework import generics
from tasks.models import Task
from django.views.generic import ListView
from tasks.serializers import TaskSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters


# Список всех задач пользователя
class MyTaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ('status', 'estimated_date')
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(responsible=user)
    def perform_create(self, serializer):
        serializer.save(responsible=self.request.user)


# Детальная информация о каждой конкретной задаче
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


# API энтрипойнт
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
    })