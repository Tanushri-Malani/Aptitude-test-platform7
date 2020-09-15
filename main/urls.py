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
    path('logical/', views.object_list, name='logical'),
    path('tts/', views.tts, name='tts'),

    ]