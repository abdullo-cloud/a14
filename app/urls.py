from django.urls import path
from .views import *



urlpatterns = [
    path('', Home.as_view(),name = "home"),
    path('about/', About.as_view(),name = "about"),
    path('contact/', Contact.as_view(),name = "contact"),
    path('myteam/', Myteam.as_view(),name = "myteam"),
    path('reklama/', Reklama.as_view(),name = "reklama"),

]

