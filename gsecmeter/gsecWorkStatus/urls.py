from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'candidate'



urlpatterns = [
    url(r'cultural/$', views.cultural, name='cultural'),
    url(r'vp/$', views.vp, name='vp'),
    url(r'^$', views.vp, name='index'),
    url(r'technical/$', views.technical, name='technical'),
    url(r'welfare/$', views.welfare, name='welfare'),
    url(r'hab/$', views.hab, name='hab'),
    url(r'sports/$', views.sports, name='sports'),

]