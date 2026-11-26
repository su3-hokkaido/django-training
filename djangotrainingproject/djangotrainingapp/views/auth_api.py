from collections.abc import Mapping

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

def request_data(request):
  # JSON が配列や文字列でもフォームが壊れないようにする
  return request.data if isinstance(request.data, Mapping) else {}

@method_decorator(ensure_csrf_cookie, name='dispatch')
class CsrfApi(APIView):
  """Issue the CSRF token cookie."""
  permission_classes = [AllowAny]

  def get(self, request):
    return Response(status=status.HTTP_204_NO_CONTENT)

class MeApi(APIView):
  """Return the logged-in user."""
  def get(self, request):
    return Response({'username': request.user.get_username()})

# DRF は未ログインのリクエストの CSRF を確認しないので、csrf_protect を付ける
@method_decorator(csrf_protect, name='dispatch')
class LoginApi(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    form = AuthenticationForm(request, data=request_data(request))
    if not form.is_valid():
      return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    login(request, form.get_user())
    return Response(status=status.HTTP_204_NO_CONTENT)

@method_decorator(csrf_protect, name='dispatch')
class RegisterApi(APIView):
  permission_classes = [AllowAny]

  def post(self, request):
    form = UserCreationForm(data=request_data(request))
    if not form.is_valid():
      return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    login(request, form.save())
    return Response(status=status.HTTP_201_CREATED)

class LogoutApi(APIView):
  def post(self, request):
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)
