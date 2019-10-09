from django.urls import path,include

from shoppingapp import views

app_name = 'shopping'

urlpatterns = [
    path('xianshi/',views.xian_shi,name='xianshi'),
    path('tuideng/',views.tui_deng,name='tuideng'),
    path('wei_deng_lu_cu_cun/',views.wei_deng_lu_cu_cun,name='wei_deng_lu_cu_cun'),
    path('den_lu_cu_cun/',views.den_lu_cu_cun,name='den_lu_cu_cun'),
    path('den_lu_xiu_gai/',views.den_lu_xiu_gai,name='den_lu_xiu_gai'),
    path('shu_ji_chuan_ru/',views.shu_ji_chuan_ru,name='shu_ji_chuan_ru'),
    path('shan_chu/',views.shan_chu,name='shan_chu'),
    path('wei_deng_lu_xui_gai/',views.wei_deng_lu_xui_gai,name='wei_deng_lu_xui_gai'),

]