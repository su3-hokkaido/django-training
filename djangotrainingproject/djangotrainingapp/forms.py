from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    # user は画面に出さず、ビュー側でログインユーザーを設定する
    fields = ['title', 'description', 'completed']
