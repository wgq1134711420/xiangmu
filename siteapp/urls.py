from django.urls import path,include

from siteapp import views

app_name = 'siteapp'

urlpatterns = [
    path('xian_shi/',views.xian_shi,name='xian_shi'),
    path('tui_deng/',views.tui_deng,name='tui_deng'),
    path('ajax/',views.ajax,name='ajax'),
    path('jie_zhang/',views.jie_zhang,name='jie_zhang'),


]