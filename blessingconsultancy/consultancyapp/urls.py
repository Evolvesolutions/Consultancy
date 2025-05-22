from django.urls import path
from . import views

urlpatterns =[
    path("",views.home,name="home"),
<<<<<<< HEAD
    path("carrier/", views.carrier, name="carrier"),
=======
    path("client/", views.client, name = "client"),
    path("service/", views.service, name = "service"),
>>>>>>> cf9ac3d0e989d76fd4fe8c3841e66866acc7467b
]