from django.db import models
from django_filters import rest_framework as filters
from simple_history.models import HistoricalRecords


# Модель задачи
class Task(models.Model):
    history = HistoricalRecords()
    created = models.DateTimeField(auto_now_add=True)
    responsible = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    description = models.TextField()
    estimated_date = models.DateField(null=True, blank=True)
    TASK_STATUS = (
        ('n', 'Новая задача'),
        ('p', 'Запланированная задача'),
        ('i', 'Задача в работе'),
        ('f', 'Завершенная задача'),
    )
    status = models.CharField(max_length=1, choices=TASK_STATUS, default='n', help_text='Статус текущей задачи')

    class Meta:
        ordering = ['created']


# Фильтрация задач по статусу и запланированной дате завершения
class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Task
        fields = ['status', 'estimated_date']
