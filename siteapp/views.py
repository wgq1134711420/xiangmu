import json
import random
from audioop import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from registerapp.models import InTheClassification, BooksOnTheTable2,User,Shopping,Site


# Create your views here.

def tui_deng(request):
    # 删除设置的cookie 回到主页的初始状态
    co = redirect('siteapp:xian_shi')
    co.set_cookie("name", max_age=0)
    co.set_cookie("pwd", max_age=0)
    return co

def xian_shi(request):

    #购物车专属携带信息
    chayidian = request.GET.get('chayidian')
    #将购物车总价直接传过来
    jia = request.GET.get('zongjine')
    if jia == '0':
        return redirect('shopping:xianshi')
    #判断是否登录 cookie 是登录信息
    cookie = request.COOKIES.get('name')
    #name是查看购物车的登录状态
    name = request.GET.get('weiyi')
    #查询购物车表中的信息
    objict = Shopping.objects.filter(user_id=cookie)
    #查询当前用户的地址信息
    di = Site.objects.filter(user_id=cookie)
    #总价
    j = []
    for i in objict:
        l =  i.get * i.quantity
        print(i.get*i.quantity)
        j.append(l)
    p = 0
    for o in j:
        p += o
    print(p)
    if cookie:
        if name:
            return render(request, 'staticapp/indent.html',{'cookie':cookie,'jia':jia,'objict':objict,'p':p,'di':di})

    return HttpResponseRedirect('/loginapp/denlu/?chayidian=chayidian')


def chuli(u):
    #对传像前端的数据对象进行格式化
    if isinstance(u,Site):
        return {'consignee':u.consignee,'fetailed':u.detailed_address,'postal':u.postal_code,'cell_phon':u.cell_phone_number}

def ajax(request):
    #拿到前端的ajax请求
    name = request.POST.get('name')
    print(name)
    #将数据转成列表传向序列化函数
    dizhi = Site.objects.filter(id=name)
    json_str = json.dumps(list(dizhi),default=chuli)
    return HttpResponse(json_str)

def jie_zhang(request):

    #接受前端传来的信息和当前登录的用户信息
    name = request.COOKIES.get('name')
    yinghu = request.GET.get('yinghu')
    dizhi = request.GET.get('dizhi')
    youxiang = request.GET.get('youxiang')
    dianhua = request.GET.get('dianhua')
    jine = request.GET.get('jine')
    #查看地址表中是否有此地址
    n = Site.objects.filter(user_id=name,consignee=yinghu,detailed_address=dizhi,postal_code=youxiang,cell_phone_number=dianhua).count()
    #将书籍的数量传向前端
    di = Shopping.objects.filter(user_id=name)
    shu = []
    for l in di:
        s = l.quantity
        shu.append(s)
    z = 0
    for j in shu:
        z +=j
    #随机生成订单编号
    a = '12345678901234567890'
    q = random.sample(a,13)
    q = ''.join(q)
    shanchu = Shopping.objects.filter(user_id=name)
    shanchu.delete()
    if n:
        return render(request,'staticapp/indent ok.html',{'jine':jine,'z':z,'yinghu':yinghu,'q':q})
    else:
        duixiang = Site(user_id=name,consignee=yinghu,detailed_address=dizhi,postal_code=youxiang,cell_phone_number=dianhua)
        duixiang.save()
        return render(request,'staticapp/indent ok.html',{'jine':jine,'z':z,'yinghu':yinghu,'q':q})

