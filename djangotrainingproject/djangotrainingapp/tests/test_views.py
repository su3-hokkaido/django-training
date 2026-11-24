from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from ..models import Task

class TaskViewTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('tester', password='pass')
    self.task = Task.objects.create(user=self.user, title='sample')

  def test_list_requires_login(self):
    response = self.client.get(reverse('tasks'))
    self.assertEqual(response.status_code, 302)

  def test_list_after_login(self):
    self.client.login(username='tester', password='pass')
    response = self.client.get(reverse('tasks'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'djangotrainingapp/task/task_list.html')

  def test_detail_template(self):
    self.client.login(username='tester', password='pass')
    response = self.client.get(reverse('task', args=[self.task.pk]))
    self.assertTemplateUsed(response, 'djangotrainingapp/task/task_detail.html')

  def test_create_and_update_template(self):
    self.client.login(username='tester', password='pass')
    for url in (reverse('task-create'), reverse('task-update', args=[self.task.pk])):
      response = self.client.get(url)
      self.assertTemplateUsed(response, 'djangotrainingapp/task/task_form.html')

  def test_delete_only_on_post(self):
    self.client.login(username='tester', password='pass')
    url = reverse('task-delete', args=[self.task.pk])
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'djangotrainingapp/task/task_confirm_delete.html')
    self.assertTrue(Task.objects.filter(pk=self.task.pk).exists())
    self.client.post(url)
    self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

class LoginViewTest(TestCase):
  def test_login_template(self):
    response = self.client.get(reverse('login'))
    self.assertTemplateUsed(response, 'djangotrainingapp/auth/login.html')

class TaskFormTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('tester', password='pass')
    self.client.login(username='tester', password='pass')

  def test_form_has_no_user_field(self):
    response = self.client.get(reverse('task-create'))
    self.assertNotIn('user', response.context['form'].fields)

  def test_create_sets_logged_in_user(self):
    self.client.post(reverse('task-create'), {'title': 'new'})
    self.assertEqual(Task.objects.get(title='new').user, self.user)

  def test_update_keeps_user(self):
    task = Task.objects.create(user=self.user, title='old')
    self.client.post(reverse('task-update', args=[task.pk]), {'title': 'changed'})
    task.refresh_from_db()
    self.assertEqual((task.title, task.user), ('changed', self.user))
