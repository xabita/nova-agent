from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from users.models import User
from .forms import UserForm


# Create your views here
def home(request):
	index_template = "app/index.html"
	
	return render(request, index_template, {
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

	