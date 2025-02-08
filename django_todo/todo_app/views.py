from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You'er at the todo_app index.")