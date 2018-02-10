from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from users.models import User

# Create your views here
def home(request):
	index_template = "app/index.html"
	
	return render(request, index_template, {
		'title_page': 'Nova-agent'
	})