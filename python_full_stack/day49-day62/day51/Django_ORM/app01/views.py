from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Book


def index(request):
    return render(request, "index.html")


def addbook(request):
    # b = Book(name="python2", price=99, author="yuan", pub_date="2017-12-12")
    # b.save()
    Book.objects.create(name="python3测试", price=99, author="yuan", pub_date="2017-12-12")
    # return render(request, )
    return HttpResponse("添加成功")


def update(request):
    Book.objects.filter(author="yuan").update(price=990)
    print(type(Book.objects.filter(author="yuan")))
    print(type(Book.objects.filter(author="yuan")[0]))
    return HttpResponse("修改成功")


def delete(request):
    Book.objects.filter(author="yuan").delete()
    return HttpResponse("删除成功")


def select(request):
    book_list = Book.objects.all()

    return render(request, "index.html", {"book_list": book_list})
