from django.urls import path

from books.views import listview

app_name = 'books'

urlpatterns = [

    path("books/", listview, name='list'),

]