from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Book


def index(request):
    return render(request, "index.html")


def addbook(request):
    b = Book(name="python2", price=99, author="yuan", pub_date="2017-12-12")
    b.save()
    # return render(request, )
    return HttpResponse("添加成功")
