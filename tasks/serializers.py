from rest_framework import serializers
from tasks.models import Task

# Возможные статусы задачи
TASK_STATUS = (
    ('n', 'Новая задача'),
    ('p', 'Запланированная задача'),
    ('i', 'Задача в работе'),
    ('f', 'Завершенная задача'),
)

# Сериализатор записей истории изменения задачи
class HistoricalRecordField(serializers.ListField):
    child = serializers.DictField()
    def to_representation(self, data):
        return super().to_representation(data.values())

# Сериализатор задач
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    responsible = serializers.ReadOnlyField(source='responsible.username')
    history = HistoricalRecordField(read_only=True)
    class Meta:
        model = Task
        fields = ['url', 'id','created', 'title', 'description', 'estimated_date', 'status', 'responsible','history']




