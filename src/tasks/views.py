from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        else:
            form = UserCreationForm()
        return render(request,'registration/register.html',{'form':form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # get_object_or_404(Task, pk=pk, user=request.user)

    # filtrage
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)

    completed = request.GET.get('completed')
    if completed:
        tasks = tasks.filter(completed=completed == 'True')

    return  render(request,'tasks/task_list.html',{'tasks':tasks})


@login_required
def task_detail(request, pk):
    tasks = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html',{'tasks':tasks})


@login_required
def task_create(request):
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_detail', pk=task.pk)
        else:
            form = TaskForm()
        return render(request, 'tasks/task_form.html',{'form':form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task,pk=pk,user=request.user)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        else:
            form=TaskForm(instance=task)
        return render(request,'tasks/task_form.html',{'form':form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task,pk=pk, user=request.user)
    if request.method =='POST':
        task.delete()
        return  redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html',{'task':task})