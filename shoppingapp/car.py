"""
购物车处理

"""
from registerapp.models import InTheClassification, BooksOnTheTable2
class Cart_items():
    """
    book:是从书籍表中查到的queruset对象
    count：书籍的总数
    """
    #book是书籍表查询到的中的queryset对象
    def __init__(self,book,count):
        self.book = book
        self.count = count



class Cart():

    def __init__(self):
        """
        total_prices:总价
        asve_price:总的优惠价格
        cart_items:储存Cart_items对象
        """
        self. total_prices = 0
        self.save_price = 0
        self.cart_items = []
    #计算总价
    def sums(self):
        """
        dna_dan_jia:是书籍表中的当当价字段
        pricing;是书籍表中的原价字段
        :return:
        """
        self.total_prices = 0
        self.save_price = 0
        self.jishu = 0
        for i in self.cart_items:
            self.jishu +=1
            self.total_prices += i.book[self.jishu-1].dna_dan_jia * i.count
            self.save_price += (i.book[self.jishu-1].pricing -  i.book[self.jishu-1].dna_dan_jia) * i.count
    #添加商品

    def add(self,id):
        self.shu = 0
        for i in self.cart_items:
            self.shu+=1
            if i.book[self.shu-1].id == id:
                i.count += 1
                self.sums()
                return
        self.cart_items.append(Cart_items(BooksOnTheTable2.objects.filter(id=id),1))
        self.sums()
    #删除书籍
    def delt(self,id):
        self.shuui = 0
        for i in self.cart_items:
            self.shuui +=1
            if i.book[self.shuui-1].id ==id:
                self.cart_items.remove(i)
                self.sums()
    #修改书籍数量
    def change(self,id,unss):
        self.shsh = 0
        for i in self.cart_items:
            self.shsh+=1
            if i.book[self.shsh-1].id == id:
                i.count = unss
                self.sums()