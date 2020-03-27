from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def show_times(request):
    t = time.ctime()
    return render(request,"index.html",{"time":t})

def article_year(request,year,month):
    return HttpResponse("this is year {0},month {1}".format(year,month))

def article_month(request,month):
    return HttpResponse("this is month{0}".format(month))

def register(request):
    return HttpResponse("register")