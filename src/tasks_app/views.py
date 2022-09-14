from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTaskForm
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def home(request):

    ## Display the list
    if "tasks_list" not in request.session:
        request.session["tasks_list"]= []

    ## Add Tasks to the list
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks_list"] += [task]
            return redirect('tasks_app:home')
    else:
        form = NewTaskForm()

    return render(request, 'tasks_app/home.html', {
        "tasks_list":request.session["tasks_list"],
        "form": form
    })

## Delete the list
def delete(request):

    if request.session["tasks_list"] != []:
        del request.session["tasks_list"]

    return redirect('tasks_app:home')

'''
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
'''
