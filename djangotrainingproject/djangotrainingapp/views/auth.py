from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class TaskListLoginView(LoginView):  # pyright: ignore[reportMissingTypeArgument]
  model = User
  context_object_name = 'task_list_login'
  fields = '__all__'
  template_name = 'djangotrainingapp/auth/login.html' # Default: 'templates/registration/login.html'
  def get_success_url(self):
    return reverse_lazy('tasks')
