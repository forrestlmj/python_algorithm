from django.shortcuts import HttpResponse
def index(req):
    print(req.GET)
    return HttpResponse("sucee")