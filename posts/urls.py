from django.urls import path

from posts.views import listview

app_name = 'posts'

urlpatterns = [

    path("", listview, name='list'),


]