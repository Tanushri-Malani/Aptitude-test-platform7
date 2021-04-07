from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.apps import apps
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

Logical = type('Logical',(models.Model,),{
    'question':models.CharField(max_length=500),
    'la':models.CharField(max_length=500),
    'lb':models.CharField(max_length=500),
    'lc':models.CharField(max_length=500),
    'ld':models.CharField(max_length=500),
    'ans':models.CharField(max_length=500),
    '__module__': __name__,
    })

Verbal = type('Verbal',(models.Model,),{
    'question':models.CharField(max_length=500),
    'la':models.CharField(max_length=500),
    'lb':models.CharField(max_length=500),
    'lc':models.CharField(max_length=500),
    'ld':models.CharField(max_length=500),
    'ans':models.CharField(max_length=500),
    '__module__': __name__,
    })

Quantitative = type('Quantitative',(models.Model,),{
    'question':models.CharField(max_length=500),
    'la':models.CharField(max_length=500),
    'lb':models.CharField(max_length=500),
    'lc':models.CharField(max_length=500),
    'ld':models.CharField(max_length=500),
    'ans':models.CharField(max_length=500),
    '__module__': __name__,
    })

Spatial = type('Spatial',(models.Model,),{
    'question':models.CharField(max_length=500),
    'la':models.ImageField(max_length=500),
    'lb':models.ImageField(max_length=500),
    'lc':models.ImageField(max_length=500),
    'ld':models.ImageField(max_length=500),
    'ans':models.CharField(max_length=500),
    '__module__': __name__,
    })

class Test(models.Model):
	total=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	def __str__(self):
		print(self.id)
		return "Test id:%s" %(self.id)

class Result(models.Model):
	user=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	final_total=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	Logical=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	Verbal=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	Spatial=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	Quantitative=models.DecimalField(max_digits=100,decimal_places=0,default=0)
	def __str__(self):
		return (str(self.user)+" : "+str(self.id))

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    head_shot=models.ImageField(upload_to='profil_images',blank=True)
    
    class Meta:
        ordering = ["user"]

    def __str__(self):
        return self.user.username