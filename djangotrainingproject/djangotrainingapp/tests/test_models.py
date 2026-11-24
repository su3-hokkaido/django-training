from django.test import TestCase

from ..models import Task

class TaskModelTest(TestCase):
  def test_str_returns_title(self):
    task = Task.objects.create(title='sample')
    self.assertEqual(str(task), 'sample')

  def test_completed_defaults_to_false(self):
    task = Task.objects.create(title='sample')
    self.assertFalse(task.completed)
