from django.shortcuts import HttpResponse
def index(req):
    print(req.GET)
    print(req.POST)
    for item in req.FILES:
        fileObj = req.FILES.get(item)
        f = open(fileObj.name,'wb')
        iter_file = fileObj.chunks()
        for line in iter_file:
            f.write(line)
        f.close()
    print(req.FILES)
    return HttpResponse("sucee")