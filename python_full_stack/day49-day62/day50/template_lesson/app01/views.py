from django.http import HttpResponse
import datetime


# Create your views here.
from django.shortcuts import render


def show_times(req):
    t = datetime.datetime.now()
    return render(req, "show_times.html", {"time": t})
#     return HttpResponse("sdfsfd")

