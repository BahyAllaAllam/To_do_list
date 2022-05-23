from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTaskForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.

# tasks_list = ["foo", "bar", "baz"]

def home(request):
    if "tasks_list" not in request.session:
        request.session["tasks_list"]= []

    return render(request, 'tasks_app/home.html', {
        "tasks_list":request.session["tasks_list"]
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks_list"] += [task]
            messages.success(request, 'The Task has been add successfully! , Refresh the page to delete the message.')
            return redirect('tasks_app:add')
    else:
        form = NewTaskForm()

    return render(request, "tasks_app/add.html", {
        "form": form
    })