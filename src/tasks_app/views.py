from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

tasks_list = ["foo", "bar", "baz"]

def home(request):
    return render(request, 'tasks_app/home.html', {
        "tasks_list":tasks_list
    })