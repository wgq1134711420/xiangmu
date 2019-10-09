import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from shoppingapp.car import Cart,Cart_items
from registerapp.models import InTheClassification, BooksOnTheTable2,User,Shopping,OrderList
# Create your views here.

def shan_chu(request):#等待修改
    name = request.GET.get('name')
    print(name,'zxc')
    s = Cart()
    s.delt(name)
    return redirect('shopping:xianshi')


def tui_deng(request):
    #删除设置的cookie 回到主页的初始状态
    co = redirect('shopping:xianshi')
    co.set_cookie("name",max_age=0)
    co.set_cookie("pwd",max_age=0)
    return co


def xian_shi(request):
    #未登录表中的信息
    shui = OrderList.objects.all()
    #未登录价格信息
    #总价
    zhongjia =[]
    for z in shui:
        zz = z.user_id
        zzz = z.shu
        zzzz = zz*zzz
        zhongjia.append(zzzz)
    zhengzongjia = 0
    for jia in zhongjia:
        zhengzongjia+=jia

    #差价
    chajiajia = []
    for c in shui:
        cc = c.shu
        ccc = c.order_amount
        cccc = cc*ccc
        chajiajia.append(cccc)
    yuanzhongjia = 0
    for chajiii in chajiajia:
        yuanzhongjia+=chajiii
    weidengluchajia = yuanzhongjia-zhengzongjia

    #总数
    weidenglushuliang = 0
    for shuliang in shui:
        weidenglushuliang+=1

    #判断是否登录
    n = request.COOKIES.get('name')
    #从session中取值
    m = request.session.get('Cart')
    l = []
    if m:
        l =m.cart_items

    #从库表中取值

    #判断当前登录的用户是谁
    user = Shopping.objects.filter(user_id=n)

    zongjia=[]#总价
    for i in user:
        ini= i.quantity
        ni= i.get
        z = ini*ni
        zongjia.append(z)
    zong = 0
    for j in zongjia:
        zong+=j


    chajia = []#差价
    for k in user:
        ss = k.id_id
        s = k.quantity
        sss = ss*s
        chajia.append(sss)
    yuan = 0
    for kk in chajia:
        yuan+=kk
    cha = yuan - zong#差价

    #购物的数量
    shu = 0
    for l in user:
        shu+=1


    #向前端传递登录状态
    D = 0
    if n:
        D = 1
    return render(request,'shoappingapp/car.html',
                  {'name':n,'cook':D,'cart':l,'cart1':m,'zong':zong,'user':user,'cha':cha,'shu':shu,'shui':shui,'zhengzongjia':zhengzongjia,'weidengluchajia':weidengluchajia,'weidenglushuliang':weidenglushuliang}
                  )


def wei_deng_lu_cu_cun(request):
    name = request.GET.get('name')
    n = OrderList.objects.filter(id=name)
    n.delete()
    return redirect('shopping:xianshi')

def den_lu_cu_cun(request):
    #删除购物车的书籍信息
    name = request.GET.get('name')
    u = Shopping.objects.filter(id=name)
    u.delete()
    return redirect('shopping:xianshi')


def wei_deng_lu_xui_gai(request):
    name = request.POST.get('name')
    print(name)
    get = request.POST.get('get')
    n = OrderList.objects.all()
    u = OrderList.objects.filter(id=name)
    for i in u:
        i.shu = get
        i.save()

    zongjia = []  # 总价
    for i in n:
        ini = i.shu
        ni = i.user_id
        z = ini * ni
        zongjia.append(z)
    zong = 0
    for j in zongjia:
        zong += j

    chajia = []
    # 差价
    for k in n:
        ss = k.order_amount
        s = k.shu
        sss = ss * s
        chajia.append(sss)
    yuan = 0
    for kk in chajia:
        yuan += kk
    cha = yuan - zong  # 差价

    # 单本书的总价
    dianbenshu = []
    for l in u:
        p = l.user_id
        pp = l.shu
        dianbenshu.append(p)
        dianbenshu.append(pp)
    zxc = int(dianbenshu[0]) * int(dianbenshu[1])
    lst = [cha, zong, zxc]

    return HttpResponse(json.dumps(lst))


def den_lu_xiu_gai(request):
    #修改购物车的书籍信息
    name = request.POST.get('name')
    get = request.POST.get('get')
    u = Shopping.objects.filter(id=name)
    for i in u:
        i.quantity=get
        i.save()
    # 拿到当前用户信息
    n = request.COOKIES.get('name')
    user = Shopping.objects.filter(user_id=n)

    zongjia = []  # 总价
    for i in user:
        ini = i.quantity
        ni = i.get
        z = ini * ni
        zongjia.append(z)
    zong = 0
    for j in zongjia:
        zong += j

    chajia = []
    # 差价
    for k in user:
        ss = k.id_id
        s = k.quantity
        sss = ss * s
        chajia.append(sss)
    yuan = 0
    for kk in chajia:
        yuan += kk
    cha = yuan - zong  # 差价

    #单本书的总价
    dianbenshu = []
    for l in u:
        p = l.get
        pp = l.quantity
        dianbenshu.append(p)
        dianbenshu.append(pp)
    zxc = int(dianbenshu[0])*int(dianbenshu[1])
    lst = [cha,zong,zxc]

    return HttpResponse(json.dumps(lst))

def shu_ji_chuan_ru(request):
    kk = request.COOKIES.get('name')

    #书籍分页的数据信息传入购物车
    name = request.POST.get('bookname')
    yuanjia = request.POST.get('bookyuanjia')
    xianjia = request.POST.get('bookxianjia')
    n = request.POST.get('name')
    m = request.POST.get('nbme')
    print(m)

    # 判断是否登录
    if kk:
        ren = Shopping.objects.filter(user_id=n).count()
        book = Shopping.objects.filter(book_id=m).count()
        # 判断此用户是否已有购物信息
        if ren != 0:

            #判断用户的信息中是否有这本书
            if book != 0:

                b = Shopping.objects.filter(isbn_id=name,user_id=n)
                for i in b:
                    i.quantity+=1
                    i.save()
            else:
                bb = Shopping(user_id=n,book_id=m,quantity=1,isbn_id=name,id_id=yuanjia,get=xianjia)
                bb.save()
        else:
            bb = Shopping(user_id=n, book_id=m, quantity=1,isbn_id=name,id_id=yuanjia,get=xianjia)
            bb.save()
    else:
        #判断得出无用户登录将书籍信息添加在session中
        shu = OrderList.objects.filter(order_time=name)
        print(shu)
        if shu :

            shuu = OrderList.objects.filter(order_time=name)
            for ii in shuu:
                ii.shu += 1
                ii.save()
        else:

            li = OrderList(id_id=n, order_reference=m, shu=1,order_time=name,order_amount=yuanjia,user_id=xianjia)
            li.save()
    return redirect('book:fenzu')

    # return HttpResponse(0)