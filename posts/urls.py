from django.urls import path

from posts.views import listview

urlpatterns = [

    path("", listview),


]