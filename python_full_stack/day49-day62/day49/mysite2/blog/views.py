from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def show_times(request):
    t = time.ctime()
    return render(request,"index.html",{"time":t})

def article_year(request):
    return HttpResponse("2004")