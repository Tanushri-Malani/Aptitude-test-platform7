from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
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


def object_list(request):
	#Model = apps.get_model('ms', model)
	olist = Logical.objects.all()
	object_list=random.sample(set(olist), 1)
	template_name='Question1.html'
	return render(request, template_name, {'object_list': object_list})

def verbal(request):
	#Model = apps.get_model('ms', model)
	olist = Verbal.objects.all()
	object_list=random.sample(set(olist), 1)
	template_name='Question2.html'
	return render(request, template_name, {'object_list': object_list})

@csrf_exempt
def tts(request):
	if request.is_ajax and request.method == "POST":
		#print("99999999999999999999999999999999999999999999999999999999999")
		question = request.POST.get("question", None)
		option1= request.POST.get("option1", None)
		option2 = request.POST.get("option2", None)
		option3 = request.POST.get("option3", None)
		option4 = request.POST.get("option4", None)
		engine = pyttsx3.init()
		engine.setProperty("rate", 170)  
		x='Question is'
		engine.say(x)
		engine.say(question)
		x="Options are "
		engine.say(x)
		engine.say("Option 1 is ")
		engine.say(option1)
		engine.say("Option 2 is ")
		engine.say(option2)
		engine.say("Option 3 is ")
		engine.say(option3)
		engine.say("Option 4 is ")
		engine.say(option4) 
		engine.say("Please speak the correct option ")
		engine.runAndWait()
		engine.stop()

		source = urllib.request.urlopen('http://127.0.0.1:8000/logical/')
		soup = BeautifulSoup(source, 'lxml')
		t=soup.find(id="q")
		print(t.text)
		print("doneeeeeeeeeeeeeeeeeeeeeeeeeeee")	
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)


def home(request):
	template_name='Home.html'
	return render(request, template_name)
    
def instructions(request):
	template_name='Instructions.html'
	return render(request, template_name)

def register(request):
	template_name='Register.html'
	return render(request, template_name)

def sec1ins(request):
	template_name='Section1Instructions.html'
	return render(request, template_name)

def sec1sub(request):
	template_name='Section1Submission.html'
	return render(request, template_name)

def sec2ins(request):
	template_name='Section2Instructions.html'
	return render(request, template_name)

def sec2sub(request):
	template_name='Section2Submission.html'
	return render(request, template_name)

def login(request):
	template_name='Login.html'
	return render(request, template_name)

def register(request):
	template_name='Register.html'
	return render(request, template_name)

