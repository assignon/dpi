from django.urls import path
from django.conf.urls import url
from hotels import views

urlpatterns = [
    path('', views.home, name="home"),
    url(r'^get_region/$', views.get_city_region, name='region'),
    url(r'^get_hotels/$', views.get_hotels, name='hotel'),
]
