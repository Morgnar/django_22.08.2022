from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def listview(request):
    return render(
        request,
        "books/books_template.html",
        {"dane": "Dane: Lista ksiazek, ksiazkowe informacje"}
    )
