from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Book


def index(request):
    return render(request, "index.html")


def addbook(request):
    Book.objects.create(name="linux运维", price=77, pub_date="2017-12-12", publish_id=2)

    return HttpResponse("添加成功")


def update(request):
    pass


def delete(request):
    pass


def select(request):
    pass

