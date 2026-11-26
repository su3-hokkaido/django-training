from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class AuthApiTest(TestCase):
  password = 'S3cure-pass-xyz'

  def setUp(self):
    User.objects.create_user('tester', password=self.password)
    self.client = APIClient()

  def post(self, name, data=None):
    return self.client.post(reverse(name), data, format='json')

  def me(self):
    return self.client.get(reverse('api-me'))

  def test_me_requires_login(self):
    self.assertEqual(self.me().status_code, 403)

  def test_login_and_logout(self):
    response = self.post('api-login', {'username': 'tester', 'password': self.password})
    self.assertEqual(response.status_code, 204)
    self.assertEqual(self.me().json(), {'username': 'tester'})

    self.assertEqual(self.post('api-logout').status_code, 204)
    self.assertEqual(self.me().status_code, 403)

  def test_login_with_wrong_password(self):
    response = self.post('api-login', {'username': 'tester', 'password': 'wrong'})
    self.assertEqual(response.status_code, 400)
    self.assertIn('__all__', response.json())
    self.assertEqual(self.me().status_code, 403)

  def test_non_object_body_returns_400(self):
    for name in ('api-login', 'api-register'):
      self.assertEqual(self.post(name, ['x']).status_code, 400, name)

  def test_register_creates_user_and_logs_in(self):
    response = self.post('api-register', {
      'username': 'newuser', 'password1': self.password, 'password2': self.password})
    self.assertEqual(response.status_code, 201)
    self.assertEqual(self.me().json(), {'username': 'newuser'})

  def test_register_rejects_mismatched_passwords(self):
    response = self.post('api-register', {
      'username': 'newuser', 'password1': self.password, 'password2': 'different-pass-1'})
    self.assertEqual(response.status_code, 400)
    self.assertIn('password2', response.json())
    self.assertFalse(User.objects.filter(username='newuser').exists())

  def test_anonymous_post_requires_csrf_token(self):
    self.client = APIClient(enforce_csrf_checks=True)
    data = {'username': 'tester', 'password': self.password}
    self.assertEqual(self.post('api-login', data).status_code, 403)
    self.assertEqual(self.post('api-register', data).status_code, 403)

  def test_login_with_csrf_token(self):
    self.client = APIClient(enforce_csrf_checks=True)
    self.assertEqual(self.client.get(reverse('api-csrf')).status_code, 204)
    response = self.client.post(
      reverse('api-login'), {'username': 'tester', 'password': self.password},
      format='json', HTTP_X_CSRFTOKEN=self.client.cookies['csrftoken'].value)
    self.assertEqual(response.status_code, 204)

  def test_logout_requires_csrf_token(self):
    self.client = APIClient(enforce_csrf_checks=True)
    self.client.login(username='tester', password=self.password)
    self.assertEqual(self.post('api-logout').status_code, 403)
    self.assertEqual(self.me().status_code, 200)
