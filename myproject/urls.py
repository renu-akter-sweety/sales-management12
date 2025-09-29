
from django.contrib import admin
from django.urls import path
from myapp.views import *
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',basepage,name='basepage'),
    path('empform/',empformpage,name='empform'),
    path('empdata/',empdatapage,name='empdata'),
    path('about/',aboutpage,name='about'),
    
]
    

