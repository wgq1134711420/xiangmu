
from django.urls import path

from registerapp import views

app_name = 'register'

urlpatterns = [
    path('xianshi/',views.zhu_ce_xian_shi,name='xianshi'),
    path('chuli/',views.zhu_ce_chu_li,name='chuli'),
    path('yan/',views.yan_zhen_gma,name='yan'),
    path('yanma/',views.yan_zheng_ma_chu_li,name='yanma'),
    path('cun/',views.cu_cun,name='cun'),
    path('zhi_jie_gou_wu/',views.zhi_jie_gou_wu,name='zhi_jie_gou_wu'),

]
