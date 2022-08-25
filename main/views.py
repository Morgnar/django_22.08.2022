from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def homepage(request):
    #template = loader.get_template("homepage.html")
    #contex = {}
    #return HttpResponse(template.render(contex, request))

    return render(
        request,
        "main/homepage.html",
        {"dane": "ALA MA KOTA"}

    )


def greetings(request):
    return  HttpResponse("Hello!!!")
