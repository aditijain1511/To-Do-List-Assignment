from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm,UpdateForm
from .models import Todo

def index(request):
	item_list = Todo.objects.order_by("-start_date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.author = request.user
			form.save()
			return redirect('todo')
	form = TodoForm()

	page = {
		"forms": form,
		"list": item_list,
		"title": "TODO LIST",
	}
	return render(request, 'toDo_list/index.html', page)

def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect('todo')

def updatedTask(request,item_id):
	queryset = Todo.objects.get(id=item_id)
	form = UpdateForm(instance=queryset)
	if request.method =='POST':
		form = UpdateForm(request.POST,instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'forms':form,
		}
	return render(request, 'toDo_list/updatedTask.html', context)
