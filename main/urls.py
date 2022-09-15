from django.urls import path

from .views import homepage, greetings

urlpatterns = [
    path("", homepage, name='home_test'),
    path("greetings/", greetings),



]