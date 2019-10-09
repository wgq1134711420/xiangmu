import random
import string
import hashlib


from django.http import HttpResponse
from django.shortcuts import render, redirect
from registerapp.captcha.image import ImageCaptcha
# Create your views here.
from registerapp.models import User, OrderList, Shopping


def yan_zhen_gma(request):
    #生成验证码
    m = ImageCaptcha()

    y = random.sample(string.ascii_letters + string.digits, 4)
    #将验证码转成字符串
    s = ''.join(y)
    #将验证码储存在session中
    request.session['sessions'] = s

    d = m.generate(s)
    return HttpResponse(d, 'm/png')


def zhu_ce_xian_shi(request):
    chayidian = request.GET.get('chayidian')
    print(chayidian,1)
    #进入注册页面
    return render(request,'registerapp/register.html',{'chayidian':chayidian})

def zhu_ce_chu_li(request):
    #接收前端发送的ajax请求
    n =  request.POST.get('name')
    #验证前端传来的值在数据库中是否存在
    m = User.objects.filter(id=n).count()

    if m == 1:
        #存在
        return HttpResponse(0)
    #不存在
    return HttpResponse(1)

def yan_zheng_ma_chu_li(request):
    #拿到前端发来的值
    n = request.POST.get('name')
    #拿到存在session中的值
    m = request.session.get('sessions')
    #进行比对查看是否一致
    if m.lower() == n.lower():
        #一致
        return HttpResponse(1)
    #不一致
    return HttpResponse(0)

def cu_cun(request):
    #接受前端的参数查看是否有购物车信息
    chayidian = request.POST.get('chayidian')
    print(chayidian)
    #接收前端的值
    n = request.POST.get('txt_username')
    m = request.POST.get('txt_password')
    #将密码进行加密
    h = hashlib.sha512()
    h.update(m.encode())
    p = h.hexdigest()
    # 设置盐 将盐存在数据库中
    s = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    yan = random.sample(s,10)
    yan = ''.join(yan)

    #将值存在数据库中

    s = User(id=n,pow=p)
    s.save()
    #将存在值当做参数发送到指定页面
    ry = redirect('shopping:xianshi')
    ry.set_cookie('name', n)
    ry.set_cookie('pwd', p)
    if chayidian != 'None' :
        ww = OrderList.objects.all()
        for j in ww:
            uu = Shopping.objects.filter(user_id=n, isbn_id=j.order_time)
            if uu:
                uu[0].quantity += 1
            else:
                uuu = Shopping(isbn_id=j.order_time, id_id=j.order_amount, user_id=n, book_id=j.order_reference,
                               quantity=j.shu, get=j.user_id)
                uuu.save()
        ww.delete()
        return ry
    else:
        return render(request,'registerapp/register ok.html',{'hao':n,'mi':p})

def zhi_jie_gou_wu(request):
    #直接跳转到主页
    n = request.GET.get('hh')
    m = request.GET.get('mm')
    #加密
    h = hashlib.sha512()
    h.update(m.encode())
    p = h.hexdigest()
    #设置cookie
    ff = redirect('homepage:xianshi')
    ff.set_cookie('name', n)
    ff.set_cookie('pwd', p)
    return ff
