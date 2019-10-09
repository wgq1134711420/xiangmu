from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from registerapp.models import InTheClassification, BooksOnTheTable2
from shoppingapp.car import Cart


def shu_ji_chuan_ru(request):

    #书籍详情页面的书籍信息加入购物车
    n = request.GET.get('name')
    m = request.GET.get('nbme')
    car = request.session.get('Cart')
    print(n,m)
    if n:
        if car:
            s = Cart()
            s.add(m)
            request.session['Cart'] = s
        else:
            cart = Cart()
            cart.add(m)
            request.session['Cart'] = cart

    pass
    return redirect('book:xianshibook')
    # return HttpResponse(0)


def tui_deng_deng(request):
    #删除设置的cookie 回到主页的初始状态
    co = redirect('book:xianshibook')
    co.set_cookie("name",max_age=0)
    co.set_cookie("pwd",max_age=0)

    return co


def xian_shi_tu_shu_jie_shao(request):

    cookie = request.COOKIES.get('name')
    id = request.GET.get('name')
    id = int(id)
    if id < 0 or id > 191:
        id = 1
    m = BooksOnTheTable2.objects.filter(id=id)
    mm=0
    for i in m:
        mm = i
    return render(request,'bookapp/Book details.html',{'Nname':cookie,'shu':mm})



def tui_deng(request):
    #删除设置的cookie 回到主页的初始状态
    co = redirect('book:fenzu')
    co.set_cookie("name",max_age=0)
    co.set_cookie("pwd",max_age=0)

    return co


def fen_lei_xian_shi(request):
    cookie = request.COOKIES.get('name')

    kk =[]
    #处理分类数据
    nn = request.GET.get('name')
    mm = request.GET.get('bnme')
    # print(nn,mm)
    if mm  is None: #总的
        # print('1')
        mm = 59
        mmame = InTheClassification.objects.filter(id=mm)
        sss = mmame[0].taxon
        kk.append(sss)
    elif nn is None :#一级
        # print(2)
        mmame = InTheClassification.objects.filter(id=mm)
        sss = mmame[0].taxon
        kk.append(sss)
    else:#二级
        # print(3)
        # print(nn,mm)
        nname = InTheClassification.objects.filter(id=nn)
        mmame = InTheClassification.objects.filter(id=mm)
        # s = nname[0].id
        # ssss = mmame[0].id
        ss = nname[0].taxon
        sss = mmame[0].taxon
        # kk.append(ssss)
        # kk.append(s)
        kk.append(ss)
        kk.append(sss)
        # print(kk)
        # print(nname,mmame,ss)



    # 分类查询 主类
    n = InTheClassification.objects.filter(taxon_id=None)
    # print(n)
    # 分类查询 从类
    m = InTheClassification.objects.filter(taxon_id__isnull=False)


    #一级
    yiji = request.GET.get('znme')
    # print(yiji)
    # 二级分类查寻分页器
    bjict = request.GET.get('snme')
    # print(bjict,'调')

    # print(ob,'调')
    if yiji != None :

        ma = request.GET.get('ma')
        l = request.GET.get('id')
        if l == None:
            l = 1
        if ma == 'm':
            ff = []
            fen = InTheClassification.objects.filter(taxon_id=yiji)
            for i in fen:
                ye = i.id
                ff.append(ye)
            yi = BooksOnTheTable2.objects.filter(classify__range=(ff[0], ff[-1])).order_by('id')
        elif ma == 'g':
            ff = []
            fen = InTheClassification.objects.filter(taxon_id=yiji)
            for i in fen:
                ye = i.id
                ff.append(ye)
            yi = BooksOnTheTable2.objects.filter(classify__range=(ff[0], ff[-1])).order_by('bei_4')
        elif ma == 'd':
            ff = []
            fen = InTheClassification.objects.filter(taxon_id=yiji)
            for i in fen:
                ye = i.id
                ff.append(ye)
            yi = BooksOnTheTable2.objects.filter(classify__range=(ff[0], ff[-1])).order_by('-pricing')
        elif ma == 's':
            ff = []
            fen = InTheClassification.objects.filter(taxon_id=yiji)
            for i in fen:
                ye = i.id
                ff.append(ye)
            yi = BooksOnTheTable2.objects.filter(classify__range=(ff[0], ff[-1])).order_by('printing_time')
        else:
        # 一级分类分页
            ff = []
            fen = InTheClassification.objects.filter(taxon_id=yiji)
            for i in fen:
                ye = i.id
                ff.append(ye)
            yi = BooksOnTheTable2.objects.filter(classify__range=(ff[0], ff[-1]))


        p = Paginator(yi, per_page=4)
        page = p.page(l)
        fenxixi = 'bnme={}'.format(mm)
        biaoshi = "znme={}".format(yiji)
        return render(request, 'bookapp/booklist.html', {'name': n, 'ename': m, 'page': page, 'kk': kk,'biaoshi':biaoshi,'fenxixi':fenxixi,'Nname':cookie})

    elif  bjict != None:

        ma = request.GET.get('ma')
        s = request.GET.get('id')
        if s == None:
            s = 1
        if ma == 'm':
            nbsp = BooksOnTheTable2.objects.filter(classify=bjict).order_by('id')
        elif ma == 'g':
            nbsp = BooksOnTheTable2.objects.filter(classify=bjict).order_by('bei_4')
        elif ma == 'd':
            nbsp = BooksOnTheTable2.objects.filter(classify=bjict).order_by('-pricing')
        elif ma == 's':
            nbsp = BooksOnTheTable2.objects.filter(classify=bjict).order_by('printing_time')
        else:
            nbsp = BooksOnTheTable2.objects.filter(classify=bjict)
        #二级分类

        p = Paginator(nbsp, per_page=4)
        page = p.page(s)
        fenxixi = 'name={}&bnme={}'.format(nn,mm)
        biaoshi = "snme={}".format(bjict)
        return render(request, 'bookapp/booklist.html', {'name': n, 'ename': m, 'page': page, 'kk': kk,'biaoshi':biaoshi,'fenxixi':fenxixi,'Nname':cookie})

    else:
        #排序
        ma =request.GET.get('ma')

        name = request.GET.get('id')
        if name == None:
            name = 1
        if ma == 'm':
            f = BooksOnTheTable2.objects.all().order_by('id')
        elif ma == 'g':
            f = BooksOnTheTable2.objects.all().order_by('bei_4')
        elif ma == 'd':
            f = BooksOnTheTable2.objects.all().order_by('-pricing')
        elif ma == 's':
            f = BooksOnTheTable2.objects.all().order_by('printing_time')
        else:
            # 分页器
            f = BooksOnTheTable2.objects.all()
        p = Paginator(f, per_page=4)
        page = p.page(name)
        biaoshi = "biao={}"


        return render(request, 'bookapp/booklist.html', {'name': n, 'ename': m, 'page': page, 'kk': kk,'biaoshi':biaoshi,'Nname':cookie})

