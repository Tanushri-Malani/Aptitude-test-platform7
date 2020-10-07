from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.apps import apps

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