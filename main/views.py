from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.apps import apps
import random
from .models import Logical,Verbal
import pyttsx3 
import speech_recognition as sr
from pocketsphinx import LiveSpeech
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import js2py
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

@login_required(login_url='/login/')
def object_list(request):
	#Model = apps.get_model('ms', model)
	olist = Logical.objects.all()
	object_list=random.sample(set(olist), 2)
	template_name='Question1.html'
	return render(request, template_name, {'object_list': object_list})

@login_required(login_url='/login/')
def verbal(request):
	#Model = apps.get_model('ms', model)
	olist = Verbal.objects.all()
	object_list=random.sample(set(olist), 2)
	template_name='Question2.html'
	return render(request, template_name, {'object_list': object_list})

@csrf_exempt
def tts(request):
	if request.is_ajax and request.method == "POST":
		#print("99999999999999999999999999999999999999999999999999999999999")
		#print(request)
		ques = request.POST.getlist("que")
		o1= request.POST.getlist("o")
		o2 = request.POST.getlist("op")
		o3 = request.POST.getlist("opt")
		o4 = request.POST.getlist("opti")
		#print(ques,ques[0])
		ques=str(ques[0])
		ques=ques.split("?")
		
		o1=str(o1[0])
		o1=o1.split("#")
		o2=str(o2[0])
		o2=o2.split("#")
		o3=str(o3[0])
		o3=o3.split("#")
		o4=str(o4[0])
		o4=o4.split("#")
		print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		#print(ques)
		item=''
		ques = [i for i in ques if i != item]
		o1 = [i for i in o1 if i != item]
		o2 = [i for i in o2 if i != item]
		o3 = [i for i in o3 if i != item]
		o4 = [i for i in o4 if i != item]
		#print(ques,option1)
		engine = pyttsx3.init()
		#engine.say("hello")
		#print("sssssssssssssssssssssssssssssssssssssssssssssssss")
		engine.setProperty("rate", 170) 
		print((ques),"lllllllllllllllllllllllllllllllllllllllllllll")
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		for i in range(0,len(ques)): 
			x='Question is'
			#print(x)
			engine.say(x)
			engine.say(ques[i])
			x="Options are "
			engine.say(x)
			engine.say("Option 1 is ")
			engine.say(o1[i])
			engine.say("Option 2 is ")
			engine.say(o2[i])
			engine.say("Option 3 is ")
			engine.say(o3[i])
			engine.say("Option 4 is ")
			engine.say(o4[i]) 
			engine.say("Please speak the correct option ")
			engine.runAndWait()
			engine.stop()
			t=5
			while t: 
				mins, secs = divmod(t, 60)
				timer = '{:02d}:{:02d}'.format(mins, secs)
				print(timer, end="\r")
				time.sleep(1)
				t -= 1

		#options = webdriver.ChromeOptions()
		#options.add_argument('--ignore-certificate-errors')
		#options.add_argument("--test-type")
		#options.binary_location = "/usr/bin/chromium"
	

	
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)


def home(request):
	template_name='Home.html'
	return render(request, template_name)
 
@login_required(login_url='/login/') 
def instructions(request):
	template_name='Instructions.html'
	return render(request, template_name)

@login_required(login_url='/login/') 
def sec1ins(request):
	template_name='Section1Instructions.html'
	return render(request, template_name)

@login_required(login_url='/login/')   
def sec1sub(request):
	template_name='Section1Submission.html'
	return render(request, template_name)

@login_required   
def sec2ins(request):
	template_name='Section2Instructions.html'
	return render(request, template_name)

@login_required   
def sec2sub(request):
	template_name='Section2Submission.html'
	return render(request, template_name)

#def login(request):
	#template_name='Login.html'
	#return render(request, template_name)

#def register(request):
	#template_name='Register.html'
	#return render(request, template_name)

def login(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			#print("7777777777777777777777777777777777777777777777777777777")
			return redirect("/")
		else:
			messages.info(request,'Invalid credentials')
			return redirect("/login/")
	else:
		return render(request,'Login.html')


def register (request):
	if  request.method == 'POST':
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		username=request.POST.get('username')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		email=request.POST.get('email')
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('/register/')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken')
				return redirect('/register/')
			else:
				user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.is_active=True
				user.save()
				print('user created')
				return redirect('/register/')
		else:
			messages.info(request,'Password not matching')
			return redirect('/register/')
		return redirect('/')
	else:
		return render(request,'Register.html')


def logout(request):
	if request.method == "POST":
		django_logout(request)
		#print("oooooooooooooooooooooooooooooooooooooooo")
		return redirect('/')

