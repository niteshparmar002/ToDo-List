from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from home.models import Task
from django.urls import reverse

# Create your views here.
def home(request):
    context = {'success' : False, 'name':'Nitesh'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(taskTitle=title, taskDescription=desc)
        ins.save()
        context = {'success' : True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.order_by("-id")
    for item in allTasks:
        print(item.taskDescription)
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)

def update(request, id):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        pi = Task.objects.get(pk=id)
        pi.taskTitle = title
        pi.taskDescription = desc
        pi.save()
        context = {'success' : True}

    else:
        pi = Task.objects.get(pk=id)
        context = {'pi':pi}
    
    return render(request, 'update.html', context)

def delete(request, id):
    if request.method == "POST":
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
