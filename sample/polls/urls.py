from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^meters/$', views.meter_list),
    url(r'^meters/(?P<pk>[0-9]+)/$', views.meter_detail),

]

