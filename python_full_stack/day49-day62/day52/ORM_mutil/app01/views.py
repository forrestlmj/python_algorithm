from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Book
from app01.models import Publish



def index(request):
    return render(request, "index.html")


def addbook(request):
    # 通过publish_id直接用外键来添加
    # Book.objects.create(name="linux运维", price=77, pub_date="2017-12-12", publish_id=2)
    # publish_obj = Publish.objects.filter(name="人民出版社")[0]
    # Book.objects.create(name="linux运维", price=79, pub_date="2017-12-12", publish=publish_obj)
    # book_obj = Book.objects.get(name="python")
    # 正向查询，通过book查询publish
    # 一对多：book_obj.publish---------一定是一个对象
    # print(book_obj.publish.name)
    # print(book_obj.publish.city)
    # print(type(book_obj.publish))
    # 反向查询，通过publish查询book
    # 查询人民出版社的书籍
    # 方式一
    # pub_object = Publish.objects.filter(name="人民出版社")[0]
    # ret = Book.objects.filter(publish=pub_object).values("name", "price")
    # print(ret)

    # 方式二
    pub_obj = Publish.objects.filter(name="人民出版社")[0]
    print(pub_obj.book_set.all())
    print(type(pub_obj.book_set.all()))

    return HttpResponse("添加成功")


def update(request):
    pass


def delete(request):
    pass


def select(request):
    pass

