from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from impact.models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
	return render(request, 'impact/index.html')

def header_info(request):
	return render(request, 'impact/header.html')

def footer_info(request):
	return render(request, 'impact/footer.html')

def aboutus_info(request):
	return render(request, 'impact/aboutus.html')

def service_info(request):
	return render(request, 'impact/service.html')

def advertisement_info(request):
	return render(request, 'impact/advertising.html')

def events_info(request):
	return render(request, 'impact/event.html')

def jobs_info(request):
	return render(request, 'impact/job.html')

def gallery_info(request):
	image_list = gallery_image.objects.all()
	context = {'image_list':image_list}
	return render(request, 'impact/gallery.html', context)

def contactus_info(request):
	return render(request, 'impact/contactus.html')

	
