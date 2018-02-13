from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from users.models import User
from .forms import UserForm


# Create your views here
def home(request):
	index_template = "app/index.html"
	list_users = User.objects.all().order_by('-created_at')
	
	return render(request, index_template, {
		'list_users': list_users,
		'title_page': 'Nova-agent'
	})

def users_new(request):
	index_template = "app/users_index.html"
	users_form = UserForm()
	
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'users_form': 'users_form',
		'form': users_form,
	})

def users_add(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			#resource_us= request.POST.get('usercourse')
			#resource_user = UserCourse.objects.get(pk=resource_us)
			#course.usercourse = resource_user
			#course.save()
			
			#UsId= request.POST.get('UserId')
			#UserId = UserCourse.objects.get(pk=UsId)
			
			return home(request, user.id)
	else:
		return redirect('home')

