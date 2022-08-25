from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def listview(request):
    return render(
        request,
        "posts/posts_template.html",
        {"dane": "Dane: Lista postow, cos o postach"}
    )
