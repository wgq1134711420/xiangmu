from django.contrib import admin
from django.urls import path,include

from homepageapp import views

app_name = 'homepage'

urlpatterns = [
    path('xianshi/',views.xian_shi,name='xianshi'),
    path('tuideng/',views.tui_deng,name='tuideng'),

]