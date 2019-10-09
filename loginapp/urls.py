from django.contrib import admin
from django.urls import path,include

from loginapp import views

app_name = 'loginapp'

urlpatterns = [
    path('denlu/',views.den_lu,name='denlu'),
    path('yan/',views.yan_zhen_gma,name='yan'),
    path('li/',views.den_lu_cu_li,name='li'),
    path('yanzheng/',views.den_li_yan_zheng,name='yanzheng'),
    path('ajax/',views.den_lu_ajax,name='ajax'),


]