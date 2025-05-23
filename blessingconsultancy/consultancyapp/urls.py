from django.urls import path
from . import views

urlpatterns =[
    path("",views.home,name="home"),
    # path("client/", views.client, name = "client"),
    path("carrier/", views.carrier, name = "carrier"),
    path('submit/',views.submit, name = "submit"),
    path('registration_success/',views.registration_success, name='registration_success'),
    path('submission/',views.submission, name = 'submission'),
    # path('carrier/success/',views.su)
]