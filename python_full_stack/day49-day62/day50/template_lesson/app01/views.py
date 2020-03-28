from django.http import HttpResponse
import datetime


# Create your views here.


def show_times(req):
    t = datetime.datetime.now()
    return HttpResponse("<html><body>It is now {0}</body></html>".format(t))
