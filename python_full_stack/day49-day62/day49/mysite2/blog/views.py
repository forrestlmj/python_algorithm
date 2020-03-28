from django.shortcuts import render, redirect, HttpResponse

import time
# Create your views here.


def show_times(request):
    t = time.ctime()
    name = "yck"
    return render(request, "index.html", locals())


def article_year(request, year, month):
    return HttpResponse("this is year {0}, month {1}".format(year, month))


def article_month(request, month):
    return HttpResponse("this is month{0}".format(month))


def register(request):
    print(request.path)
    print(request.GET.get("user"))
    print(request.GET.get("age"))
    print(request.GET.get("hobby"))
    a = 1
    if request.method == "POST":
        user = request.POST.get("user")
        if user == "yck":
            return redirect("/blog/login/")
        return HttpResponse("success post")
    return render(request,  "register.html")


def login(request):
    return render(request, "login.html")
