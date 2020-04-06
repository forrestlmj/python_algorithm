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
    publish_obj = Publish.objects.filter(name="人民出版社")[0]
    Book.objects.create(name="linux运维", price=79, pub_date="2017-12-12", publish=publish_obj)
    return HttpResponse("添加成功")


def update(request):
    pass


def delete(request):
    pass


def select(request):
    pass

