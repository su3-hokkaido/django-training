from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):  # type: ignore
  class Meta:
    model = Task
    # user は入力させず、ビュー側でログインユーザーを設定する
    fields = ['id', 'title', 'description', 'completed']
