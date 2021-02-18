from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.apps import apps
import random
from .models import Logical,Verbal,Test,Result,Quantitative,Spatial
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

from django.apps import apps
from main.utils import *

@login_required(login_url='/login/')
def object_list(request):
	#Model = apps.get_model('ms', model)
	try:
		n=request.session['noofques']
	except:
		n=1
	new_result=Result()
	new_result.save()
	request.session['result_id']=new_result.id
	olist = Logical.objects.all()
	object_list=random.sample(set(olist), n)
	template_name='Question1.html'
	mod='Logical'
	return render(request, template_name, {'object_list': object_list,'mod': mod})


@login_required(login_url='/login/')
def verbal(request):
	#Model = apps.get_model('ms', model)
	try:
		n=request.session['noofques']
	except:
		n=1
	olist = Verbal.objects.all()
	object_list=random.sample(set(olist), n)
	template_name='Question2.html'
	mod='Verbal'
	return render(request, template_name, {'object_list': object_list,'mod': mod})

@login_required(login_url='/login/')
def quantitative(request):
	#Model = apps.get_model('ms', model)
	try:
		n=request.session['noofques']
	except:
		n=1
	olist = Quantitative.objects.all()
	object_list=random.sample(set(olist), n)
	template_name='Question4.html'
	mod='Quantitative'
	return render(request, template_name, {'object_list': object_list,'mod': mod})

@login_required(login_url='/login/')
def spatial(request):
	#Model = apps.get_model('ms', model)
	try:
		n=request.session['noofques']
	except:
		n=1
	olist = Spatial.objects.all()
	object_list=random.sample(set(olist), n)
	template_name='Question3.html'
	mod='Spatial'
	return render(request, template_name, {'object_list': object_list,'mod': mod})


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
		model= request.POST.get('mod')
		Model= apps.get_model('main',model)
		
		if model=="Logical":
			ss='sec1sum'
		elif model=="Verbal":
			ss='sec2sum'
		elif model=="Spatial":
			ss='sec3sum'
		elif model=="Quantitative":
			ss='sec4sum'
		#print(ss,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		#print(answ,"ffffffffffffffffffffffffffffffffffffffffffff")
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
		#print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		#print(ques)
		item=''
		ques = [i for i in ques if i != item]
		o1 = [i for i in o1 if i != item]
		o2 = [i for i in o2 if i != item]
		o3 = [i for i in o3 if i != item]
		o4 = [i for i in o4 if i != item]
		#print(ques,"2222222222222222222222222222222")
		engine = pyttsx3.init()
		#engine.say("hello")
		#print("sssssssssssssssssssssssssssssssssssssssssssssssss")
		engine.setProperty("rate", 300) 
		#print((ques),"lllllllllllllllllllllllllllllllllllllllllllll")
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		#answe=[]
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
			t=2
			while t: 
				mins, secs = divmod(t, 60)
				timer = '{:02d}:{:02d}'.format(mins, secs)
				print(timer, end="\r")
				time.sleep(1)
				t -= 1
			
			
			z=str(o1[i])
			#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			if z[0]==",":
				o1[i]=o1[i][1:]
			#print("ggggggggggggggggggggggggggggggggggggggggggg",ques[i])
			answe=Model.objects.filter(la=o1[i])
			print(answe,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
			a='b'
			
			try:
				the_id=request.session['test_id']
				the_rid=request.session['result_id']
				s1s=request.session[ss]
				test=Test.objects.get(id=the_id)
			except:
				the_id=None

			#print(the_id,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",s1s)
			if str(answe[0].ans)==a:
				s1s=s1s+1
				#print("++++++++++++++++!!1111111111111")
				request.session[ss]=s1s
		
		#print(request.session[ss],"sssssssssssssssssssssssssssssssssssssss",ss)
			#print(answe[0].ans,s1s,"fffffffffffffffffffffffffffffffffff")
			#b=answe
			#if a==str(answe.ans):
			#	request.session['sec1sum']=request.session['sec1sum']+1
		#print(request.session['sec1sum'])

		#options = webdriver.ChromeOptions()
		#options.add_argument('--ignore-certificate-errors')
		#options.add_argument("--test-type")
		#options.binary_location = "/usr/bin/chromium"

		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)


@csrf_exempt
def tts_s(request):
	if request.is_ajax and request.method == "POST":
		#print("99999999999999999999999999999999999999999999999999999999999")
		#print(request)
		ques = request.POST.getlist("que")
		o1= request.POST.getlist("o")
		o2 = request.POST.getlist("op")
		o3 = request.POST.getlist("opt")
		o4 = request.POST.getlist("opti")
		model= request.POST.get('mod')
		Model= apps.get_model('main',model)
		
		if model=="Logical":
			ss='sec1sum'
		elif model=="Verbal":
			ss='sec2sum'
		elif model=="Spatial":
			ss='sec3sum'
		elif model=="Quantitative":
			ss='sec4sum'
		#print(ss,"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		#print(answ,"ffffffffffffffffffffffffffffffffffffffffffff")
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
		#print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		#print(ques)
		item=''
		ques = [i for i in ques if i != item]
		o1 = [i for i in o1 if i != item]
		o2 = [i for i in o2 if i != item]
		o3 = [i for i in o3 if i != item]
		o4 = [i for i in o4 if i != item]
		#print(ques,"2222222222222222222222222222222")
		engine = pyttsx3.init()
		#engine.say("hello")
		#print("sssssssssssssssssssssssssssssssssssssssssssssssss")
		engine.setProperty("rate", 300) 
		#print((ques),"lllllllllllllllllllllllllllllllllllllllllllll")
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		#answe=[]
		

		for i in range(0,len(ques)): 
			z=str(o1[i])
			#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			if z[0]==",":
				o1[i]=o1[i][1:]
			z=str(o2[i])
				#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			if z[0]==",":
				o2[i]=o2[i][1:]
			z=str(o3[i])
				#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			if z[0]==",":
				o3[i]=o3[i][1:]
			z=str(o4[i])
			#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			if z[0]==",":
				o4[i]=o4[i][1:]
			x='Question is'
			#print(x)
			engine.say(x)
			engine.say(ques[i])
			x="Options are "
			engine.say(x)
			engine.say("Option 1 is ")
			engine.say(predict(o1[i]))
			engine.say("Option 2 is ")
			engine.say(predict(o2[i]))
			engine.say("Option 3 is ")
			engine.say(predict(o3[i]))
			engine.say("Option 4 is ")
			engine.say(predict(o4[i])) 
			engine.say("Please speak the correct option ")
			engine.runAndWait()
			engine.stop()
			t=2
			while t: 
				mins, secs = divmod(t, 60)
				timer = '{:02d}:{:02d}'.format(mins, secs)
				print(timer, end="\r")
				time.sleep(1)
				t -= 1
			
			
			#z=str(o1[i])
			o1[i]=o1[i].split("/")
			#print(z,"llllllllllllllllllllllllllllllllllllllllllllllll")
			o1[i]=o1[i][-1]
			#print("ggggggggggggggggggggggggggggggggggggggggggg",o1[i])
			answe=Model.objects.filter(la=o1[i])
			#print(answe,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
			a='b'
			
			try:
				the_id=request.session['test_id']
				the_rid=request.session['result_id']
				s1s=request.session[ss]
				test=Test.objects.get(id=the_id)
			except:
				the_id=None

			#print(answe[0].ans,"iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",a)
			if str(answe[0].ans)==a:
				#print("heyyyyy")
				s1s=s1s+1
				#print("++++++++++++++++!!1111111111111")
				request.session[ss]=s1s
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)

def home(request):
	template_name='Home.html'
	return render(request, template_name)


@login_required(login_url='/login/') 
def pscores(request):
	s=Result.objects.filter(user=request.user)
	template_name='Pscores.html'
	return render(request, template_name,{'s':s})

 
@login_required(login_url='/login/') 
def instructions(request):
	new_test=Test()
	new_test.save()
	request.session['test_id']=new_test.id
	#print(new_test.id)
	#print(request.session['test_id'],"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
	request.session['sec1sum']=0
	request.session['sec2sum']=0
	request.session['sec3sum']=0
	request.session['sec4sum']=0
	request.session['noofques']=2
	the_id=new_test.id
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


@login_required(login_url='/login/')  
def sec2ins(request):
	template_name='Section2Instructions.html'
	return render(request, template_name)


@login_required(login_url='/login/')
def sec2sub(request):
	template_name='Section2Submission.html'
	return render(request, template_name)

@login_required(login_url='/login/') 
def sec3ins(request):
	template_name='Section3Instructions.html'
	return render(request, template_name)

@login_required(login_url='/login/')
def sec3sub(request):
	print("sec3sub,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
	template_name='Section3Submission.html'
	return render(request, template_name)

@login_required(login_url='/login/') 
def sec4ins(request):
	template_name='Section4Instructions.html'
	return render(request, template_name)

@login_required(login_url='/login/')   
def sec4sub(request):
	template_name='Section4Submission.html'
	return render(request, template_name)

@login_required(login_url='/login/') 
def result(request):
	try:
		the_id=request.session['test_id']
		the_rid=request.session['result_id']
		s1s=request.session['sec1sum']
		s2s=request.session['sec2sum']
		s3s=request.session['sec3sum']
		s4s=request.session['sec4sum']
		total=s1s+s2s+s3s+s4s
		r=Result.objects.get(id=the_rid)
		print(r.Logical,"lllllllllllllllllllllllllllllrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		r.user=request.user
		r.final_total=total
		r.Logical=s1s
		print(r.Logical,"llllllllllllllllllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",s1s)
		r.Verbal=s2s
		r.Spatial=s3s
		r.Quantitative=s4s
		r.save()
		test=Test.objects.get(id=the_id)
		test.delete()
		print("deleted test after checking results")
	except:
		print("Not able to finish test while checking results")
		pass
	template_name='result.html'
	return render(request, template_name,{'s1s': s1s,'s2s': s2s,'s3s':s3s,'s4s':s4s,'total': total})

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
	try:
		the_id=request.session['test_id']
		the_rid=request.session['result_id']
		test=Test.objects.get(id=the_id)
		test.delete()
		result=Result.objects.get(id=the_rid)
		result.delete()
		print("ids found and deleted after logout")
	except:
		print("both the ids not found after logout")
	if request.method == "POST":
		django_logout(request)
		#print("oooooooooooooooooooooooooooooooooooooooo")
		return redirect('/')

@login_required(login_url='/login/') 
def tts_repeat(request):
	#print("888888888888888888888888888888888888888888888888888888")
	if request.is_ajax and request.method == "POST":
		#print("99999999999999999999999999999999999999999999999999999999999")
		#print(request)
		ques = request.POST.getlist("que")
		o1= request.POST.getlist("o")
		o2 = request.POST.getlist("op")
		o3 = request.POST.getlist("opt")
		o4 = request.POST.getlist("opti")

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
		#print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
		#print(ques)
		item=''
		ques = [i for i in ques if i != item]
		o1 = [i for i in o1 if i != item]
		o2 = [i for i in o2 if i != item]
		o3 = [i for i in o3 if i != item]
		o4 = [i for i in o4 if i != item]
		#print(ques,"2222222222222222222222222222222")
		engine = pyttsx3.init()
		#engine.say("hello")
		#print("sssssssssssssssssssssssssssssssssssssssssssssssss")
		engine.setProperty("rate", 300) 
		#print((ques),"lllllllllllllllllllllllllllllllllllllllllllll")
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		#answe=[]
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
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrreeeeeeeeeeeeeeeeeeeeeeee")
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)

@csrf_exempt
@login_required(login_url='/login/')
def tts1(request):
	#print("88888888888888888888888888888888888888888888")
	if request.is_ajax and request.method == "POST":
		#print("99999999999999999999999999999999999999999999999999999999999")
		#print(request)
		ques = request.POST.getlist("que")
		buts = request.POST.getlist("but")
		#print(buts)
		ques=str(ques[0])
		buts=str(buts[0])

		ques=ques.split("?")
		buts=buts.split("?")

		item=''
		ques = [i for i in ques if i != item]
		buts = [i for i in buts if i != item]

		item='Submit1'
		buts = [i for i in buts if i != item]
		print(buts)

		engine = pyttsx3.init()
		engine.setProperty("rate", 200)
		#print(engine)
		#engine.say("hello hi")
		#print("sssssssssssssssssssssssssssssssssssssssssssssssss")
		#print((ques),"lllllllllllllllllllllllllllllllllllllllllllll")
		#print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
		#answe=[]
		for i in range(0,len(ques)):
			z=str(ques[i])
			if z[0]==",":
				ques[i]=ques[i][1:]
			engine.say(ques[i])
		

		if len(buts)>1:
			engine.say("There are "+str(len(buts))+" buttons, they are")
			for i in range(0,len(buts)):
				z=str(buts[i])
				if z[0]==",":
					buts[i]=buts[i][1:]
				engine.say(buts[i])
		else:
			engine.say("There is "+str(len(buts))+" button, it is")
			z=str(buts[0])
			if z[0]==",":
				buts[0]=buts[0][1:]
			engine.say(buts[0])
		
		engine.runAndWait()
		engine.stop()
		#print(ques,"ffffffffffffffffffffffffffff")
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)