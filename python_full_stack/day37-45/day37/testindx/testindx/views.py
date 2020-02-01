from django.shortcuts import HttpResponse
def index(req):
    print(req.GET)
    print(req.POST)
    print(req.FILES)
    return HttpResponse("sucee")