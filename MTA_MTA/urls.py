from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('django.views.generic.simple',

    # index 'home page' of the appname e.g. webtest
    url(r'^$', views.index, name='<appname>_index'),

    url(r'^stack_preview/(?P<imageId>[0-9]+)/$', views.stack_preview, name="<appname>_stack_preview"),

    url(r'^justapage', views.justapage),

    url(r'^test_template_3columns', views.test_template_3columns),


    url(r'^mta/(?P<imageId>[0-9]+)/$', views.mta, name="<appname>_mta"),

    url(r'^getImage/(?P<imageId>[0-9]+)/$', views.getImage),

    url(r'^testAjax/(?P<z>[0-9]+)/$', views.testAjax),

    url(r'^loadTree/$', views.loadTree),

    url(r'^intensityAnalysis/(?P<datasetId>[0-9]+)$', views.intensityAnalysis),

    url(r'^segmentImage/(?P<iid>[0-9]+)/(?P<z>[0-9]+)/(?P<c>[0-9]+)/(?P<t>[0-9]+)/(?P<minSize>[0-9]+)$', views.segmentImage),

    url(r'^measure/(?P<iid>[0-9]+)/(?P<c>[0-9]+)/(?P<minSize>[0-9]+)$', views.measure)



 )


# loadTree = (r'^loadTree', views.loadTree)
