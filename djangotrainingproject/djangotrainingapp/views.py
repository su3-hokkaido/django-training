from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render

# Create your views here.
def task_list(request: HttpRequest) -> HttpResponse:
  return HttpResponse('<h1>Hello, Django!!!</h1>')
