from django.http import HttpResponse
import datetime


# Create your views here.
from django.shortcuts import render


def show_times(req):
    t = datetime.datetime.now()
    return render(req, "show_times.html", {"time": t})
#     return HttpResponse("sdfsfd")


def query(request):
    # render函数中context参数可以是字典，列表
    action = ["村长", "louisck"]
    d = {"name": "louisck", "age": 46, "hobby": "jerk off"}
    return render(request, "index.html", locals())

