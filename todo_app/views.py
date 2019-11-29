from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        messages.success(request,("New Task Added"))
        return redirect('todolist') 
    else:
        all_tasks = Task.objects.filter(user=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks' : all_tasks})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.user == request.user:
        task.delete()
    else:
        messages.error(request,("Access Restricted!"))

    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Edited"))
        return redirect('todolist') 
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj' : task_obj})

@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task.user == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request,("Access Restricted!"))
        
    return redirect('todolist')

@login_required
def incomplete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')