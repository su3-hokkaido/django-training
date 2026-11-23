from django.views.generic.list import ListView
from djangotrainingapp.models import Task

# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = "tasks"
