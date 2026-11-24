from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .models import User

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
  model = Task
  context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  context_object_name = 'task_create'
  # fields = ['id', 'title', 'description']
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  context_object_name = 'task_update'
  fields = '__all__'
  success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
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
