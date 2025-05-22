from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def carrier(request):
    return render(request, "carrier.html")