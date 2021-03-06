from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from users.models import User
from ciudades.models import Ciudad
from .forms import UserForm


# Create your views here
def home(request):
	index_template = "app/index.html"
	list_users = User.objects.all()

	return render(request, index_template, {
		'list_users': list_users,
		'title_page': 'Nova-agent'
	})

def users_new(request):
	index_template = "app/users_new.html"
	users_form = UserForm()
	ls_ciudades = User.objects.all()
    
	return render(request, index_template, {
		'title_page': 'Nuts.',
		'users_form': 'users_form',
		'ls_ciudades': 'ls_ciudades',
		'form': users_form,
	})


def users_add(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			User = form.save(commit=False)
			User.save()
			
			
			return home(request)
	else:
		return redirect('home')


def users_profile(request, pk):
	index_template = "app/users_profile.html"
	users_data = User.objects.filter(pk=pk).order_by('-created_at')
	return render(request, index_template, {
		'users_data': users_data,
		'title_page': 'Nova-agent'
	})

'''
def users_activate(request, pk):
	index_template = "app/users_update.html"

	users_data = User.objects.get(pk=pk)
	users_data.us_isactive =True
	users_data.save()

	return render(request, index_template, {
		'users_data': users_data,
		'MyCourses': MyCourses,
		'noCourses': noCourses,
		'title_page': 'Nuts'
	})

def users_update_pass(request, pk):
	index_template = "app/users_update.html"

	users_data = User.objects.get(pk=pk)
	users_data.username =True
	users_data.password =True
	users_data.save()

	return render(request, index_template, {
		'users_data': users_data,
		'MyCourses': MyCourses,
		'noCourses': noCourses,
		'title_page': 'Nuts'
	})

'''

