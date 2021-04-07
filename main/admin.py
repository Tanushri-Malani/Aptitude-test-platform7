from django.contrib import admin
from main.models import Logical,Verbal,Test,Result,Quantitative,Spatial,UserProfile

admin.site.register(Logical)
admin.site.register(Verbal)
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Quantitative)
admin.site.register(Spatial)
admin.site.register(UserProfile)