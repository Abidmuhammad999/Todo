from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def taskList(request):
    return HttpResponse("welcome")
def index(request):
    return render(request,'index.html')