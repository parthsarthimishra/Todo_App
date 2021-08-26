from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import TodoList
from .models import TodoItem
from .form import form_item


# Create your views here.

def index(request):
    """Shows the Main page of todo-App containing Lists."""
    todolists = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('todo/index.html')
    context = {
        'todolists': todolists,
    }
    return render(request, 'todo/index.html', context)

def detail(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list
    }
    return render(request, 'todo/details.html', context)

def create(request):
    if request.method == "GET":
        return render(request, 'todo/createlist.html')

    name = request.POST["name"]
    if name:
        TodoList.objects.create(list_name=name)
        lists = TodoList.objects.all()
        context = {
            'todolists': lists,
        }  
        return render(request,'todo/index.html',context)
    else:
        raise Http404("Empty field")    

def edit(request,list_id,item_id):
    try:
        todoitem = TodoItem.objects.get(id=item_id)
    except TodoItem.DoesNotExist:
        raise Http404("This Item Does not Exists")
    form_data= form_item(instance=todoitem)
    if request.method == "POST":
        form_data=form_item(request.POST,instance=todoitem)
        if form_data.is_valid():
            form_data.save()
            return redirect(f'/todo/{list_id}')
        else:
            raise Http404("Invalid Inputs")        
    form = form_item()
    context = {
        "item" : form_data
    }
    return render(request, 'todo/edit.html', context)

def delete_item(request,list_id,item_id):
    try:
        todoitem = TodoItem.objects.get(id=item_id)
    except TodoItem.DoesNotExist:
        raise Http404("This Item Does not Exists")
    todoitem.delete()
    return redirect(f'/todo/{list_id}')

def create_item(request,list_id):
    todolist = TodoList.objects.get(id=list_id)
    if request.method == "POST":
        form_data=form_item(request.POST)
        if form_data.is_valid():
            object = form_data.save(commit=False)
            object.todo_list = todolist
            object.save()
            return redirect(f'/todo/{list_id}')
        else:
            raise Http404("Invalid Inputs")    
    form_data = form_item()
    context = {
        "item_for_add" : form_data
    }
    return render(request, 'todo/createitem.html', context)

def edit_list(request,list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This Item Does not Exists")
    if request.method == "GET":
        context ={
            'todo_list_name' : todolist,
        }
        return render(request, 'todo/editlist.html', context)

    name = request.POST["name"]
    if name:
        todolist.list_name = name
        todolist.save()
        lists = TodoList.objects.all()
        context = {
            'todolists': lists,
        }
        return render(request,'todo/index.html',context)   
    else:
        raise Http404("Empty field")
def delete_list(request , list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This List Does not Exists")
    if request.method == "GET":
        todolist.delete()
    return redirect(f"/todo/")
