from django.shortcuts import render
from django.contrib import messages

from .forms import TaskForm
from .models import Task

def index(request):
    item_list = Task.objects.order_by("-date")
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TaskForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'taskmate/index.html', page)

def remove(request, item_id):
    item = Task.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('taskmate_app')
