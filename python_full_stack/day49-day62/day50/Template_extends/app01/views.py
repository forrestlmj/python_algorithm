from django.shortcuts import render

# Create your views here.


def backend(request):

    return render(request, "base.html")


def student(request):
    student_list = ["yck", "louis ck"]
    return render(request, "student2.html", locals())
