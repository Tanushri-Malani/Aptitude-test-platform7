from django.contrib import admin
from django.urls import path,include,re_path
from . import views,models
from django.conf.urls import url



#from . import views, settings
#from django.contrib.staticfiles.urls import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static
#from users import views as user_views
#from ms.views import template_list as a
app_name='main'

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.login),
    #url(r'repeat/(?P<id>\d+)/',views.repeat,name='repeat')
    path('pscores/', views.pscores, name='pscores'),
    path('logical/', views.object_list, name='logical'),
    path('quantitative/', views.quantitative, name='quantitative'),
    path('spatial/', views.spatial, name='spatial'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    url('logout/', views.logout, name='logout'),
    path('verbal/',views.verbal,name='verbal'),
    path('tts/', views.tts, name='tts'),
    path('tts_s/', views.tts_s, name='tts_s'),
    path('tts1/', views.tts1, name='tts1'),
    path('cam/', views.cam, name='cam'),
    path('tts_repeat/', views.tts_repeat, name='tts_repeat'),
    path('home/', views.home, name='home'),
    path('instructions/', views.instructions, name='instructions'),
    path('register/', views.register, name='register'),
    path('sec1ins/', views.sec1ins, name='sec1ins'),
    path('sec3ins/', views.sec3ins, name='sec3ins'),
    path('sec1sub/', views.sec1sub, name='sec1sub'),
    path('sec3sub/', views.sec3sub, name='sec3sub'),
    path('sec2ins/', views.sec2ins, name='sec2ins'),
    path('sec4ins/', views.sec4ins, name='sec4ins'),
    path('sec2sub/', views.sec2sub, name='sec2sub'),
    path('sec4sub/', views.sec4sub, name='sec4sub'),
    path('result/', views.result, name='result'),
    
    ]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)