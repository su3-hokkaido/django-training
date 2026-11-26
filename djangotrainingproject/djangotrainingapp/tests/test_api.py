from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from ..models import Task

class TaskApiTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user('tester', password='pass')
    self.other = User.objects.create_user('other', password='pass')
    self.mine = Task.objects.create(user=self.user, title='mine')
    self.theirs = Task.objects.create(user=self.other, title='theirs')
    self.client = APIClient()
    self.client.login(username='tester', password='pass')

  def detail_url(self, task):
    return reverse('api-task-detail', args=[task.pk])

  def test_requires_login(self):
    self.client.logout()
    response = self.client.get(reverse('api-task-list'))
    self.assertEqual(response.status_code, 403)

  def test_anonymous_cannot_read_or_write_a_task(self):
    self.client.logout()
    url = self.detail_url(self.mine)
    for method in ('get', 'put', 'patch', 'delete'):
      response = getattr(self.client, method)(url, {'title': 'hacked'}, format='json')
      self.assertEqual(response.status_code, 403, method)
    response = self.client.post(reverse('api-task-list'), {'title': 'new'}, format='json')
    self.assertEqual(response.status_code, 403)
    self.assertEqual(
      list(Task.objects.order_by('pk').values_list('title', flat=True)), ['mine', 'theirs'])

  def test_list_shows_only_own_tasks(self):
    response = self.client.get(reverse('api-task-list'))
    self.assertEqual(response.json(), [
      {'id': self.mine.pk, 'title': 'mine', 'description': None, 'completed': False}])

  def test_search_by_title(self):
    Task.objects.create(user=self.user, title='shopping')
    response = self.client.get(reverse('api-task-list'), {'search-text': 'SHOP'})
    self.assertEqual([task['title'] for task in response.json()], ['shopping'])

  def test_create_ignores_user_in_request(self):
    response = self.client.post(
      reverse('api-task-list'), {'title': 'new', 'user': self.other.pk}, format='json')
    self.assertEqual(response.status_code, 201)
    self.assertEqual(Task.objects.get(title='new').user, self.user)

  def test_create_requires_title(self):
    response = self.client.post(reverse('api-task-list'), {'title': ''}, format='json')
    self.assertEqual(response.status_code, 400)
    self.assertIn('title', response.json())

  def test_update_keeps_user(self):
    response = self.client.patch(self.detail_url(self.mine), {'title': 'changed'}, format='json')
    self.assertEqual(response.status_code, 200)
    self.mine.refresh_from_db()
    self.assertEqual((self.mine.title, self.mine.user), ('changed', self.user))

  def test_delete(self):
    response = self.client.delete(self.detail_url(self.mine))
    self.assertEqual(response.status_code, 204)
    self.assertFalse(Task.objects.filter(pk=self.mine.pk).exists())

  def test_others_task_returns_404(self):
    url = self.detail_url(self.theirs)
    for method in ('get', 'put', 'patch', 'delete'):
      response = getattr(self.client, method)(url, {'title': 'hacked'}, format='json')
      self.assertEqual(response.status_code, 404, method)
    self.theirs.refresh_from_db()
    self.assertEqual(self.theirs.title, 'theirs')

  def test_write_requires_csrf_token(self):
    client = APIClient(enforce_csrf_checks=True)
    client.login(username='tester', password='pass')
    response = client.post(reverse('api-task-list'), {'title': 'new'}, format='json')
    self.assertEqual(response.status_code, 403)
