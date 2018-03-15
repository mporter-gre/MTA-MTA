from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('django.views.generic.simple',

     # index 'home page' of the appname e.g. webtest
     url(r'^$', views.index, name='<appname>_index'),

     url(r'^stack_preview/(?P<imageId>[0-9]+)/$', views.stack_preview, name="<appname>_stack_preview"),

     url(r'^test_template', views.test_template)

 )