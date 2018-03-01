from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('django.views.generic.simple',

     # index 'home page' of the appname e.g. webtest
     url(r'^$', views.index, name='<appname>_index'),

 )