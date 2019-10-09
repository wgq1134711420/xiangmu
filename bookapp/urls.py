from django.contrib import admin
from django.urls import path,include

from bookapp import views

app_name = 'book'

urlpatterns = [
    path('xianshibook/',views.xian_shi_tu_shu_jie_shao,name='xianshibook'),
    path('fenzu/',views.fen_lei_xian_shi,name='fenzu'),
    path('tuideng/',views.tui_deng,name='tuideng'),
    path('tui_deng_deng/',views.tui_deng_deng,name='tui_deng_deng'),
    path('shu_ji_chuan_ru/',views.shu_ji_chuan_ru,name='shu_ji_chuan_ru'),

]