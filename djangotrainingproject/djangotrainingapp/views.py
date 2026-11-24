from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import Task
from .models import User

# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = 'tasks'

class TaskDetail(DetailView):
  model = Task
  context_object_name = 'task'

class TaskCreate(CreateView):
  model = Task
  context_object_name = 'task_create'
  # fields = ['id', 'title', 'description']
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
  model = Task
  context_object_name = 'task_update'
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
  model = Task
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')

class TaskListLoginView(LoginView):  # pyright: ignore[reportMissingTypeArgument]
  model = User
  context_object_name = 'task_list_login'
  fields = '__all__'
  template_name = 'djangotrainingapp/login.html' # Default: 'templates/registration/login.html'
  def get_success_url(self):
    return reverse_lazy('tasks')
