import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect
from registerapp.captcha.image import ImageCaptcha
import random
import string
from registerapp.models import User, OrderList, Shopping


# Create your views here.


def yan_zhen_gma(request):
    #验证码 生成
    m = ImageCaptcha()

    y = random.sample(string.ascii_letters + string.digits, 4)
    #将生成的列表转成字符串
    s = ''.join(y)
    #将生成的验证码存到session中
    request.session['sessionss'] = s

    d = m.generate(s)
    return HttpResponse(d, 'm/png')


def den_lu(request):
    #检查是否有购物车信息
    chayidian = request.GET.get('chayidian')
    print(chayidian,1)
    #检查是否有cookie 如果有直接跳转到主页
    N = request.COOKIES.get('name')
    M = request.COOKIES.get('pwd')

    if N:
        return redirect('homepage:xianshi')
    return render(request,'loginapp/login.html',{'chayidian':chayidian})

def den_lu_cu_li(request):
    #接受前方发来的ajax信息验证和储存的验证码是否一致  检查完成返回信息
    n = request.POST.get('yanzheng')
    m = request.session.get('sessionss')

    if n.lower() == m.lower():
        return HttpResponse(1)
    return HttpResponse(0)
def den_lu_ajax(request):
    chayidian = request.POST.get('chayidian')
    #接受前方发来的ajax请求 利用发来的值当做条件去数据库中查寻检查是信息否存在
    n = request.POST.get('yonghu')

    m = request.POST.get('mima')
    h = hashlib.sha512()
    h.update(m.encode())
    p = h.hexdigest()

    hao = User.objects.filter(id=n, pow=p).count()
    if hao == 1:
        #存在返回
        return HttpResponse(1)
    else:
        #不存在返回
        return HttpResponse(0)
def den_li_yan_zheng(request):
    # 判断是否有从购物车传来的信息
    chayidian = request.POST.get('chayidian')
    print(chayidian, 2)
    n = request.POST.get('txtUsername')
    m = request.POST.get('txtPassword')
    #加密
    h = hashlib.sha512()
    h.update(m.encode())
    p = h.hexdigest()
    # 从前端拿到值 进行判断 查看是否选择了七天免登陆
    t = request.POST.get('autologin')
    if t:
        # 选择了设置cookie时加上时间
        request.session['session'] = 1
        re = redirect('homepage:xianshi')
        re.set_cookie('name',n,max_age=7*24*60*60)
        re.set_cookie('pwd',p,max_age=7*24*60*60)
        rt = redirect('shopping:xianshi')
        rt.set_cookie('name',n,max_age=7*24*60*60)
        rt.set_cookie('pwd',p,max_age=7*24*60*60)
        if chayidian != 'None':
            w = OrderList.objects.all()
            for i in w:
                u = Shopping.objects.filter(user_id=n,isbn_id=i.order_time)
                if u:
                    u[0].quantity+=1
                else:
                    uu = Shopping(isbn_id=i.order_time,id_id=i.order_amount,user_id=n,book_id=i.order_reference,quantity=i.shu,get=i.user_id)
                    uu.save()
            w.delete()
            return rt
        else:
            return re
    else:
        # 判断是否有从购物车传来的信息
        request.session['session'] = 1
        ss = redirect("homepage:xianshi")
        ss.set_cookie('name', n)
        ss.set_cookie('pwd', p)
        ry = redirect('shopping:xianshi')
        ry.set_cookie('name', n)
        ry.set_cookie('pwd', p)
        if chayidian != 'None':
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
            return ss


