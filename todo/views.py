from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse


from django.contrib.auth.decorators import login_required

from todo.models import TodoList
from .forms import TaskCreation

# Create your views here.

@ login_required
def List(request):
    lists=request.user.author.all()
    context={'lists':lists}
    return render(request,'todo/list.html',context)


@login_required

def create(request):
    form=TaskCreation()
    context={'form':form}
    
    if request.method=='POST':
        form=TaskCreation(data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return HttpResponseRedirect(reverse('todo:list'))
    return render(request,'todo/create.html',context)

@login_required

def update(request,pk):
    task=TodoList.objects.get(pk=pk)
    form=TaskCreation(instance=task)
    if request.method=='POST':
        form=TaskCreation(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:list'))
    context={'form':form}
    return render(request,'todo/test.html',context)

@login_required

def delete(request,pk):
    task=TodoList.objects.get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('todo:list'))
