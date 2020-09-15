from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.apps import apps
import random
from .models import Logical
import pyttsx3 


def object_list(request):
	#Model = apps.get_model('ms', model)
	olist = Logical.objects.all()
	object_list=random.sample(set(olist), 1)
	template_name='Question1.html'
	return render(request, template_name, {'object_list': object_list})





def tts(request):
	if request.is_ajax and request.method == "GET":
		print("99999999999999999999999999999999999999999999999999999999999")
		question = request.GET.get("question", None)
		option1= request.GET.get("option1", None)
		option2 = request.GET.get("option2", None)
		option3 = request.GET.get("option3", None)
		option4 = request.GET.get("option4", None)
		engine = pyttsx3.init()  
		x='Question is'
		engine.say(x)
		engine.say(question)
		x="Options are "
		engine.say(x)
		engine.say(option1)
		engine.say(option2)
		engine.say(option3)
		engine.say(option4) 
		engine.say("Please speak the correct option ")
		engine.runAndWait()
		engine.stop()
		return JsonResponse({}, status = 200)
	else:
		return JsonResponse({}, status = 400)



    
