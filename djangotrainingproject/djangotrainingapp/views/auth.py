from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

class TaskListLoginView(LoginView):  # pyright: ignore[reportMissingTypeArgument]
  model = User
  context_object_name = 'task_list_login'
  fields = '__all__'
  template_name = 'djangotrainingapp/auth/login.html' # Default: 'templates/registration/login.html'
  def get_success_url(self):
    return reverse_lazy('tasks')

class RegisterView(FormView): # type: ignore
  template_name = 'djangotrainingapp/auth/register.html'
  form_class = UserCreationForm
  success_url = reverse_lazy('tasks')

  def form_valid(self, form):
    user = form.save()
    login(self.request, user)
    return super().form_valid(form)
