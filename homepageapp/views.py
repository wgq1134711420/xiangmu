from django.shortcuts import render, redirect

# Create your views here.
from registerapp.models import BooksOnTheTable2, InTheClassification


def tui_deng(request):
    #删除设置的cookie 回到主页的初始状态
    co = redirect('homepage:xianshi')
    co.set_cookie("name",max_age=0)
    co.set_cookie("pwd",max_age=0)

    return co


def xian_shi(request):
    #检查是否登录
    N = request.COOKIES.get('name')

    #分类查询 主类
    n  = InTheClassification.objects.filter(taxon_id=None)
    # print(n)
    # 分类查询 从类
    m = InTheClassification.objects.filter(taxon_id__isnull=False)
    # print(m)
    #范围查询 id 1-10
    s = BooksOnTheTable2.objects.filter(id__range=(1,9))
    # print(s)
    k = BooksOnTheTable2.objects.filter(id__range=(10,21))
    x = BooksOnTheTable2.objects.filter(id__range=(20,30))

    return render(request, 'homepageapp/index.html',{'name':n,'isname':m,'idname':s,'zuname':k,'xname':x,'Nname':N})