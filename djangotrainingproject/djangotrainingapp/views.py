from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from djangotrainingapp.models import Task

# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = "tasks"

class TaskDetail(DetailView):
  model = Task
  context_object_name = "task"
