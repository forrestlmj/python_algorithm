from django.shortcuts import render, HttpResponse

import time
# Create your views here.


def show_times(request):
    t = time.ctime()
    name = "yck"
    return render(request, "index.html", {"time": t, "name": name})


def article_year(request, year, month):
    return HttpResponse("this is year {0}, month {1}".format(year, month))


def article_month(request, month):
    return HttpResponse("this is month{0}".format(month))


def register(request):
    print(request.path)
    print(request.GET.get("user"))
    print(request.GET.get("age"))
    print(request.GET.get("hobby"))
    if request.method == "POST":
        return HttpResponse("success")
    return render(request,  "register.html")
