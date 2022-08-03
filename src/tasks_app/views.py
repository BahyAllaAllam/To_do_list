from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTaskForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.

## Display the list
def home(request):
    if "tasks_list" not in request.session:
        request.session["tasks_list"]= []

    return render(request, 'tasks_app/home.html', {
        "tasks_list":request.session["tasks_list"]
    })

## Add Tasks to the list
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

## Delete the list
def delete(request):
    if request.session["tasks_list"] != []:
        del request.session["tasks_list"]
        messages.success(request, "The list has been deleted successfully!")
    else:
        messages.info(request, "The list is already empty")
    return redirect('tasks_app:home')

## Testing the browser
def cookie_session(request):
    request.session.set_test_cookie()
    return render(request, "tasks_app/test.html")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = True
    else:
        response = False

    return render(request, "tasks_app/delete_test.html", {'response':response})