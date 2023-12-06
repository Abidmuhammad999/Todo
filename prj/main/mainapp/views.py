from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task
# Create your views here.
class TaskList(ListView):
    model=Task
    # return HttpResponse('Hi How are you')
    # return render(request, 'index.html')
    # template_name = "index.html"