from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import TaskForm
from ..models import Task
from .mixins import OwnerQuerysetMixin

class TaskList(LoginRequiredMixin, OwnerQuerysetMixin, ListView):
  model = Task
  template_name = 'djangotrainingapp/task/task_list.html'
  context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, OwnerQuerysetMixin, DetailView):
  model = Task
  template_name = 'djangotrainingapp/task/task_detail.html'
  context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  template_name = 'djangotrainingapp/task/task_form.html'
  context_object_name = 'task_create'
  form_class = TaskForm
  success_url = reverse_lazy('tasks')

  def form_valid(self, form): # type: ignore
    form.instance.user = self.request.user # type: ignore
    return super().form_valid(form) # type: ignore

class TaskUpdate(LoginRequiredMixin, OwnerQuerysetMixin, UpdateView):
  model = Task
  template_name = 'djangotrainingapp/task/task_form.html'
  context_object_name = 'task_update'
  form_class = TaskForm
  success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, OwnerQuerysetMixin, DeleteView):
  model = Task
  template_name = 'djangotrainingapp/task/task_confirm_delete.html'
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')
