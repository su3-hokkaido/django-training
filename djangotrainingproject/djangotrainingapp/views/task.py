from rest_framework import viewsets

from ..models import Task
from ..serializers import TaskSerializer
from .mixins import OwnerQuerysetMixin

class TaskViewSet(OwnerQuerysetMixin, viewsets.ModelViewSet):  # type: ignore
  """API to list, retrieve, create, update and delete tasks."""
  queryset = Task.objects.all()
  serializer_class = TaskSerializer

  def perform_create(self, serializer):  # type: ignore
    serializer.save(user=self.request.user)  # type: ignore
