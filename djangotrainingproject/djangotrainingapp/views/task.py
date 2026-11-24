from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms import TaskForm
from ..models import Task

class TaskList(LoginRequiredMixin, ListView):
  model = Task
  template_name = 'djangotrainingapp/task/task_list.html'
  context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
  model = Task
  template_name = 'djangotrainingapp/task/task_detail.html'
  context_object_name = 'task'

class TaskCreate(LoginRequiredMixin, CreateView):
  model = Task
  template_name = 'djangotrainingapp/task/task_form.html'
  context_object_name = 'task_create'
  form_class = TaskForm
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
  model = Task
  template_name = 'djangotrainingapp/task/task_form.html'
  context_object_name = 'task_update'
  form_class = TaskForm
  success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
  model = Task
  template_name = 'djangotrainingapp/task/task_confirm_delete.html'
  context_object_name = 'task'
  success_url = reverse_lazy('tasks')
